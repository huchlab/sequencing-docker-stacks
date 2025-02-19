# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
from tests.conftest import TrackedContainer
from tests.R_library_check import load_library

import pytest

library_list = [
    "SingleCellExperiment",
    "monocle",
    "MAST",
    "scater",
    "scran",
    "Seurat",
]


@pytest.mark.parametrize("library", library_list)
def test_load_R_library(container: TrackedContainer, library: str) -> None:
    """Check whether R library can be loaded."""
    load_library(container, library)