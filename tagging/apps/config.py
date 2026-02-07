# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    registry: str = ""
    owner: str = ""
    image: str = ""
    variant: str = ""
    platform: str = ""

    tags_dir: Path = Path()
    hist_lines_dir: Path = Path()
    manifests_dir: Path = Path()

    repository: str = ""
    
    # Optional: source image to run for inspection (if different from full_image)
    source_image: str = ""

    def full_image(self) -> str:
        return f"{self.registry}/{self.owner}/{self.image}"
    
    def run_image(self) -> str:
        """Returns the image to use for running containers (for inspection)."""
        return self.source_image if self.source_image else self.full_image()
