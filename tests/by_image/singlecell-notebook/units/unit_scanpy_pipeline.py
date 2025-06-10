import scanpy as sc

adata = sc.datasets.blobs()

sc.pp.highly_variable_genes(adata)
sc.pp.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.tl.leiden(adata)
sc.tl.rank_genes_groups(adata, "leiden")

sc.pl.umap(adata)
