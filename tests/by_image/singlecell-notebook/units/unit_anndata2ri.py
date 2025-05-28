import anndata2ri
import scanpy as sc
import scipy as sp

adata = sc.AnnData(X=sp.sparse.csr_matrix([[0.0, 1.0], [1.0, 0.0]]))
anndata2ri.py2rpy(adata)
