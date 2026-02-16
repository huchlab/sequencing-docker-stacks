#!/usr/bin/env python3
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import logging
import os

import plumbum

from tagging.apps.common_cli_arguments import common_arguments_parser
from tagging.apps.config import Config
from tagging.utils.get_prefix import get_file_prefix_for_platform

crane = plumbum.local["crane"]

LOGGER = logging.getLogger(__name__)


def copy_and_tag_image(
    config: Config,
    source_registry: str,
    source_owner: str,
    source_image_tag: str,
    push_to_registry: bool,
) -> None:
    """
    Copy an image directly from source registry to target registry and tag.
    Uses crane to copy without pulling to local.
    """
    LOGGER.info(f"Copying and tagging image: {config.image}")

    # Read tags from file
    file_prefix = get_file_prefix_for_platform(
        platform=config.platform, variant=config.variant
    )
    filename = f"{file_prefix}-{config.image}.txt"
    tags = (config.tags_dir / filename).read_text().splitlines()

    source_image = f"{source_registry}/{source_owner}/sequencing-docker-stacks/{config.image}:{source_image_tag}"
    LOGGER.info(f"Source image: {source_image}")

    tag0 = tags[0]
    tag_name0 = tag0.rsplit(":", 1)[-1]
    target_tag0 = f"{config.registry}/{config.owner}/{config.image}:{tag_name0}"
    LOGGER.info(f"Copying to first tag: {target_tag0}")
    copy_args = [
        "copy",
        source_image,
        target_tag0,
    ]

    if push_to_registry:
        crane[copy_args] & plumbum.FG

    # Use 'crane tag' for all subsequent tags
    # This is an instant API call with no data transfer.
    for tag in tags[1:]:
        # Extract just the tag part (after the last colon)
        # Tags are in format: registry/owner/image:tag
        tag_name = tag.rsplit(":", 1)[-1]
        target_tag = f"{config.registry}/{config.owner}/{config.image}:{tag_name}"
        LOGGER.info(f"Tagging : {target_tag}")

        tag_args = [
            "tag",
            target_tag0,
            tag_name,
        ]

        if push_to_registry:
            crane[tag_args] & plumbum.FG

    if push_to_registry:
        LOGGER.info(f"All tags copied and pushed to registry for image: {config.image}")
    else:
        LOGGER.info(f"Dry-run completed for image: {config.image}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    config = common_arguments_parser(
        registry=True,
        owner=True,
        image=True,
        variant=True,
        platform=True,
        tags_dir=True,
    )

    # Get source registry info from environment
    source_registry = os.environ.get("SOURCE_REGISTRY", "ghcr.io")
    source_owner = os.environ.get(
        "SOURCE_OWNER", os.environ.get("GITHUB_REPOSITORY_OWNER", "")
    )
    source_image_tag = os.environ.get("SOURCE_IMAGE_TAG", "")
    push_to_registry = os.environ.get("PUSH_TO_REGISTRY", "false").lower() == "true"

    if not source_image_tag:
        raise ValueError("SOURCE_IMAGE_TAG environment variable must be set")

    copy_and_tag_image(
        config, source_registry, source_owner, source_image_tag, push_to_registry
    )
