import numpy as np
import scanpy as sc

sc.settings.datasetdir = "./work/"

adata = sc.datasets.pbmc3k()

sc.pp.normalize_per_cell(adata)
sc.pp.log1p(adata)
sc.pp.pca(adata)

X = adata.obsm["X_pca"].copy()


for i in range(2):
    print(i)
    sc.pp.pca(adata)
    try:
        np.testing.assert_equal(X, adata.obsm["X_pca"])
    except AssertionError:
        raise AssertionError(
            f"Re-computed PCA for dense is not the same. Maximum absolute difference: {np.abs(X - adata.obsm['X_pca']).max()}"
        )
