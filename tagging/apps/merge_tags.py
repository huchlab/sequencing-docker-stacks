#!/usr/bin/env python3
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import logging
import os

import plumbum
from tenacity import (  # type: ignore
    RetryError,
    retry,
    stop_after_attempt,
    wait_exponential,
)

from tagging.apps.common_cli_arguments import common_arguments_parser
from tagging.apps.config import Config
from tagging.utils.get_platform import ALL_PLATFORMS
from tagging.utils.get_prefix import get_file_prefix_for_platform

docker = plumbum.local["docker"]

LOGGER = logging.getLogger(__name__)

# Get environment variables for GHCR source registry
GHCR_REGISTRY = os.environ.get("GHCR_REGISTRY", "ghcr.io")
GHCR_OWNER = os.environ.get("GHCR_OWNER", os.environ.get("OWNER", ""))
COMMIT_SHA = os.environ.get("COMMIT_SHA", "")
RUN_ID = os.environ.get("GITHUB_RUN_ID", "")


def read_local_tags_from_files(config: Config) -> set[str]:
    LOGGER.info(f"Read tags from file(s) for image: {config.image}")

    merged_local_tags = set()
    for platform in ALL_PLATFORMS:
        LOGGER.info(f"Reading tags for platform: {platform}")

        file_prefix = get_file_prefix_for_platform(
            platform=platform, variant=config.variant
        )
        filename = f"{file_prefix}-{config.image}.txt"
        path = config.tags_dir / filename
        if not path.exists():
            LOGGER.info(f"Tag file: {path} doesn't exist")
            continue

        LOGGER.info(f"Tag file: {path} found")
        for tag in path.read_text().splitlines():
            merged_local_tags.add(tag.replace(platform + "-", ""))

    LOGGER.info(f"Tags read for image: {config.image}")
    return merged_local_tags


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4))
def inspect_manifest(tag: str) -> None:
    LOGGER.info(f"Inspecting manifest for tag: {tag}")
    docker["buildx", "imagetools", "inspect", tag] & plumbum.FG
    LOGGER.info(f"Manifest {tag} exists")


def get_ghcr_source_tag(config: Config, platform: str) -> str:
    """Construct GHCR source image tag for a platform."""
    return (
        f"{GHCR_REGISTRY}/{GHCR_OWNER}/sequencing-docker-stacks/{config.image}:"
        f"build-{COMMIT_SHA}-{RUN_ID}-{platform}-{config.variant}"
    )


def find_platform_source_tags(config: Config) -> list[str]:
    """Find platform-specific source images in GHCR."""
    platform_tags = []

    for platform in ALL_PLATFORMS:
        platform_tag = get_ghcr_source_tag(config, platform)
        LOGGER.info(f"Checking for source image: {platform_tag}")
        try:
            inspect_manifest(platform_tag)
            platform_tags.append(platform_tag)
            LOGGER.info(f"Source image {platform_tag} found successfully")
        except RetryError:
            LOGGER.warning(f"Source image {platform_tag} doesn't exist in GHCR")

    return platform_tags


def apply_tags_to_manifest(
    config: Config, platform_source_tags: list[str], target_tags: set[str], push_to_registry: bool
) -> None:
    """Apply tags to a multi-arch manifest using GHCR source images."""
    if not platform_source_tags:
        LOGGER.warning("No platform source tags found, skipping all tag applications")
        return
    
    for tag in target_tags:
        LOGGER.info(f"Creating multi-arch manifest for tag: {tag}")
        
        # Construct full target tag
        target_tag = f"{config.registry}/{config.owner}/{config.image}:{tag}"
        
        args = [
            "buildx",
            "imagetools",
            "create",
            *platform_source_tags,
            "--tag",
            target_tag,
        ]
        if not push_to_registry:
            args.append("--dry-run")

        LOGGER.info(f"Running command: docker {' '.join(args)}")
        docker[args] & plumbum.FG
        
        if push_to_registry:
            LOGGER.info(f"Successfully created and pushed multi-arch manifest: {target_tag}")
        else:
            LOGGER.info(f"Dry-run: Would create and push manifest: {target_tag}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    config = common_arguments_parser(
        registry=True, owner=True, image=True, variant=True, tags_dir=True
    )
    push_to_registry = os.environ.get("PUSH_TO_REGISTRY", "false").lower() == "true"

    LOGGER.info(f"Merging tags for image: {config.image}")
    LOGGER.info(f"Source registry: {GHCR_REGISTRY}/{GHCR_OWNER}/sequencing-docker-stacks")
    LOGGER.info(f"Target registry: {config.registry}/{config.owner}")
    LOGGER.info(f"Commit SHA: {COMMIT_SHA}, Run ID: {RUN_ID}")

    # Find platform-specific source images in GHCR
    platform_source_tags = find_platform_source_tags(config)
    
    if not platform_source_tags:
        LOGGER.error("No platform source images found in GHCR. Cannot proceed.")
        if push_to_registry:
            raise RuntimeError("No platform source images found to create manifests")
        else:
            LOGGER.info("Dry-run mode: would have failed due to missing source images")
    else:
        # Read target tags from files
        target_tags = read_local_tags_from_files(config)
        LOGGER.info(f"Found {len(target_tags)} unique tags to apply")
        
        # Apply all tags to the multi-arch manifest
        apply_tags_to_manifest(config, platform_source_tags, target_tags, push_to_registry)

    LOGGER.info(f"Successfully processed tags for image: {config.image}")
