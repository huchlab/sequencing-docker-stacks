# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.

# Test scVI-tools with CUDA support
import torch
import scvi

print("scVI-tools version:", scvi.__version__)
print("PyTorch CUDA available:", torch.cuda.is_available())

# Test that scvi can use CUDA if available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device for scvi: {device}")

# Create a simple synthetic dataset for testing
import anndata
import numpy as np

n_obs = 100
n_vars = 50
X = np.random.negative_binomial(5, 0.3, size=(n_obs, n_vars))
adata = anndata.AnnData(X)

print(f"Created test AnnData: {adata.shape}")

# Setup scVI model (this tests the integration)
scvi.model.SCVI.setup_anndata(adata)
model = scvi.model.SCVI(adata)
print("scVI model created successfully")

# Train for a few epochs to verify functionality
model.train(max_epochs=1, train_size=0.9, check_val_every_n_epoch=1)
print("scVI model training test passed!")

print("scVI-tools CUDA test completed successfully!")
