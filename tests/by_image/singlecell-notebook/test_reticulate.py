"""
test_reticulate
~~~~~~~~~~~~~~~
This test module tests whether reticulate can discover and use Python.
"""

import logging

from tests.utils.conda_package_helper import CondaPackageHelper
from tests.utils.tracked_container import TrackedContainer

LOGGER = logging.getLogger(__name__)


def test_reticulate(container: TrackedContainer) -> None:
    """Test whether reticulate can discover and use Python."""

    R_script = (
        "library(reticulate); "  # load reticulate
        "cfg <- py_discover_config(); "  # discover Python
        'if (is.null(cfg)) stop("No Python discovered. `py_discover_config()` returns NULL"); '  # fail if no Python
        'expected_python <- "/opt/conda/bin/python"; '  # expected path
        "stopifnot(cfg$python == expected_python); "  # check Python
        "tryCatch({ "
        '    py_run_string("import math"); '  # <- indented inside braces
        '    message("Python command succeeded"); '
        "}, error = function(e) { "
        '    stop("Python command failed: ", e$message); '
        "})"
    )

    CondaPackageHelper(
        container
    )  # for some reason this is needed to allow container.exec_cmd to work properly
    container.exec_cmd(f"R --slave -e '{R_script}'")
