# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
from tests.conftest import TrackedContainer
from tests.import_library_check import import_library

import pytest

library_list = [
    "anndata",
    "anndata2ri",
    "arboreto",
    "bbknn",
    "celltypist",
    "decoupler",
    "gseapy",
    "harmonypy",
    "leidenalg",
    "loompy",
    "louvain",
    "mudata",
    "muon",
    "openpyxl",
    "pybiomart",
    "igraph",
    "scanorama",
    "scanpy",
    "scirpy",
    "scrublet",
    "scvi",
    "session_info"
]


@pytest.mark.parametrize("library", library_list)
def test_import_library(container: TrackedContainer, library: str) -> None:
    """Check whether R library can be loaded."""
    import_library(container, library)