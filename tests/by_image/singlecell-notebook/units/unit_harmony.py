"""Test harmonypy reproducibility.

See https://github.com/slowkow/harmonypy/issues/24
"""

import harmonypy as hm
import numpy as np
import scanpy as sc

adata = sc.datasets.blobs()

sc.pp.pca(adata)

harmony_out = hm.run_harmony(adata.obsm["X_pca"], adata.obs, "blobs")

X_harmony = harmony_out.Z_corr

adata.obsm["X_pca_harmony"] = X_harmony.copy()

for i in range(2):
    print(i)
    harmony_out = hm.run_harmony(adata.obsm["X_pca"], adata.obs, "blobs")
    X_harmony = harmony_out.Z_corr
    try:
        np.array_equal(X_harmony, adata.obsm["X_pca_harmony"])
    except AssertionError as exc:
        max_diff = np.abs(X_harmony - adata.obsm["X_pca_harmony"]).max()
        raise AssertionError(
            f"Re-computed Harmony is not the same. Maximum absolute difference: {max_diff}"
        ) from exc
