import spatialdata
from packaging import version  # type: ignore

current_version = spatialdata.__version__
required_version = "0.7.2"

# Compare versions logically
assert version.parse(current_version) > version.parse(
    required_version
), f"spatialdata version {current_version} is not higher than {required_version}"

print(f"Check passed! Current version: {current_version}")
