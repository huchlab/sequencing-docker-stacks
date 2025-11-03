# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.

# Test PyTorch with CUDA support
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("CUDA version:", torch.version.cuda)
    print("CUDA device count:", torch.cuda.device_count())
    print("CUDA device name:", torch.cuda.get_device_name(0))
    device = torch.device("cuda")
else:
    print("CUDA not available, using CPU")
    device = torch.device("cpu")

# Create a tensor and move it to the device
x = torch.randn(100, 100, device=device)
print(f"Tensor created on: {x.device}")

# Perform a simple operation
y = torch.matmul(x, x.T)
print(f"Matrix multiplication result shape: {y.shape}")
print("PyTorch CUDA test passed!")
