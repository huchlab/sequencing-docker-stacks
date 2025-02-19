# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
from dataclasses import dataclass, field

from tagging.manifests import (
    AptPackagesManifest,
    CondaEnvironmentManifest,
    JuliaPackagesManifest,
    ManifestInterface,
    RPackagesManifest,
    SparkInfoManifest,
)
from tagging.taggers import (
    DateTagger,
    JavaVersionTagger,
    JuliaVersionTagger,
    JupyterHubVersionTagger,
    JupyterLabVersionTagger,
    JupyterNotebookVersionTagger,
    PythonMajorMinorVersionTagger,
    PythonVersionTagger,
    PytorchVersionTagger,
    RVersionTagger,
    SHATagger,
    SparkVersionTagger,
    TaggerInterface,
    TensorflowVersionTagger,
    UbuntuVersionTagger,
)


@dataclass
class ImageDescription:
    parent_image: str | None
    taggers: list[TaggerInterface] = field(default_factory=list)
    manifests: list[ManifestInterface] = field(default_factory=list)


ALL_IMAGES = {
    "rnaseq-notebook": ImageDescription(
        parent_image=None,
        taggers=[
            SHATagger(),
            DateTagger(),
            UbuntuVersionTagger(),
            PythonMajorMinorVersionTagger(),
            PythonVersionTagger(),
            JupyterNotebookVersionTagger(),
            JupyterLabVersionTagger(),
            JupyterHubVersionTagger(),
            RVersionTagger()
        ],
        manifests=[
            CondaEnvironmentManifest(),
            AptPackagesManifest(),
            RPackagesManifest()
        ],
    ),
    "singlecell-notebook": ImageDescription(
        parent_image=None,
        taggers=[
            SHATagger(),
            DateTagger(),
            UbuntuVersionTagger(),
            PythonMajorMinorVersionTagger(),
            PythonVersionTagger(),
            JupyterNotebookVersionTagger(),
            JupyterLabVersionTagger(),
            JupyterHubVersionTagger(),
            RVersionTagger()
        ],
        manifests=[
            CondaEnvironmentManifest(),
            AptPackagesManifest(),
            RPackagesManifest()
        ],
    ),
    "spatial-notebook": ImageDescription(
        parent_image="singlecell-notebook"
    ),
}
