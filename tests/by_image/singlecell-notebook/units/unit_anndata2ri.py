from anndata import AnnData
from anndata2ri import converter
from rpy2.robjects import globalenv
from rpy2.robjects.conversion import localconverter
from scipy.sparse import csr_matrix

adata = AnnData(X=csr_matrix([[0.0, 1.0], [1.0, 0.0]]))

# Python2R
with localconverter(converter):
    globalenv["sce"] = adata
