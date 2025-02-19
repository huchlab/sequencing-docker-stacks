# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
from tests.conftest import TrackedContainer
from tests.R_library_check import load_library

import pytest

library_list = [
    "apeglm",
    "ashr",
    "BiocParallel",
    "biomaRt",
    "ComplexHeatmap",
    "DESeq2",
    "pheatmap",
    "plotly",
    "RColorBrewer",
    "readxl",
    "RobustRankAggreg",
    "scales",
    "scuttle",
    "tidyverse",
    "viridis",
    "vsn",
    "writexl"
]

@pytest.mark.parametrize("library", library_list)
def test_load_R_library(container: TrackedContainer, library: str) -> None:
    """Check whether R library can be loaded."""
    load_library(container, library)