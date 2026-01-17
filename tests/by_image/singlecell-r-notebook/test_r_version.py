"""
test_r_version
~~~~~~~~~~~~~~
This test module verifies that R version is >= 4.5 in singlecell-r-notebook.
"""

import logging

from tests.utils.conda_package_helper import CondaPackageHelper
from tests.utils.tracked_container import TrackedContainer

LOGGER = logging.getLogger(__name__)


def test_r_version(container: TrackedContainer) -> None:
    """Test whether R version is >= 4.5."""

    R_script = (
        "r_version <- getRversion(); "  # get R version
        "message('R version: ', r_version); "  # print version
        "if (r_version < '4.5') stop('R version is ', r_version, ' but should be >= 4.5'); "  # fail if < 4.5
        "message('R version check passed');"
    )

    CondaPackageHelper(container)
    container.exec_cmd(f"R --slave -e '{R_script}'")
