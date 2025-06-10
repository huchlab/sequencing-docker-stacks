# harmonypy: reproducibility
# see https://github.com/slowkow/harmonypy/issues/24
import numpy as np
import scanpy as sc
from scipy.cluster.vq import kmeans2

adata = sc.datasets.blobs()


def cluster_fn(
    data: np.typing.NDArray[np.float64], K: int
) -> np.typing.NDArray[np.float64]:
    """Custom clustering function for Harmony integration."""
    centroid, label = kmeans2(data, K, minit="++", seed=0)
    return centroid


sc.pp.pca(adata)
sc.external.pp.harmony_integrate(adata, "blobs", cluster_fn=cluster_fn)

X_harmony = adata.obsm["X_pca_harmony"].copy()

for i in range(2):
    print(i)
    sc.external.pp.harmony_integrate(adata, "blobs", cluster_fn=cluster_fn)
    try:
        np.testing.assert_equal(X_harmony, adata.obsm["X_pca_harmony"])
    except AssertionError:
        max_diff = np.abs(X_harmony - adata.obsm["X_pca_harmony"]).max()
        raise AssertionError(
            f"Re-computed Harmony is not the same. Maximum absolute difference: {max_diff}"
        )
