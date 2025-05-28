import numpy as np
from scipy.sparse import random
from sklearn.decomposition import PCA

np.random.seed(42)
X = random(
    2700,
    32738,
    density=2286884 / (2700 * 32738),
    format="csr",
    dtype="int32",
    data_rvs=lambda s: np.random.randint(0, 501, size=s),
)

pca_ = PCA(n_components=50, svd_solver="arpack", random_state=0)
X_pca_0 = pca_.fit_transform(X).copy()


for i in range(2):
    print(i)
    pca_ = PCA(n_components=50, svd_solver="arpack", random_state=0)
    X_pca = pca_.fit_transform(X).copy()
    try:
        np.testing.assert_equal(X_pca_0, X_pca)
    except AssertionError:
        raise AssertionError(
            f"Re-computed PCA is not the same. Maximum absolute difference: {np.abs(X_pca_0 - X_pca).max()}"
        )
