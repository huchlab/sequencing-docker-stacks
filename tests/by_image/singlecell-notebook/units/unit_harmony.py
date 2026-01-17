"""Test harmonypy reproducibility.

See https://github.com/slowkow/harmonypy/issues/24
"""

import numpy as np
import scanpy as sc

adata = sc.datasets.blobs()

sc.pp.pca(adata)
sc.external.pp.harmony_integrate(adata, "blobs")

X_harmony = adata.obsm["X_pca_harmony"].copy()

for i in range(2):
    print(i)
    sc.external.pp.harmony_integrate(adata, "blobs")
    try:
        np.testing.assert_equal(X_harmony, adata.obsm["X_pca_harmony"])
    except AssertionError as exc:
        max_diff = np.abs(X_harmony - adata.obsm["X_pca_harmony"]).max()
        raise AssertionError(
            f"Re-computed Harmony is not the same. Maximum absolute difference: {max_diff}"
        ) from exc
