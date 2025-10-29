# Jupyter Notebook Singlecell Stack - CUDA 12 Variant

This is a CUDA-enabled variant of the singlecell-notebook image with GPU acceleration support.

## Features

This variant includes all packages from the base singlecell-notebook plus:

- **CUDA 12.8**: NVIDIA CUDA Toolkit for GPU computing
- **RAPIDSai**: GPU-accelerated data science libraries including:
  - cuDF: GPU-accelerated DataFrame operations
  - cuML: GPU-accelerated machine learning algorithms
  - cuGraph: GPU-accelerated graph analytics
- **PyTorch with CUDA**: GPU-enabled deep learning framework for neural networks
- **scVI-tools with CUDA**: GPU-accelerated single-cell variational inference

## Requirements

To use this image, you need:

1. NVIDIA GPU with CUDA Compute Capability 6.0 or higher
2. NVIDIA Driver version 525.60.13 or higher
3. NVIDIA Container Toolkit installed on your host

## Usage

```bash
docker run --gpus all -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work \
  quay.io/huchlab/singlecell-notebook:cuda12-latest
```

The `--gpus all` flag enables GPU access for the container.

## Verification

To verify GPU access within the container:

```python
import torch

print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA devices: {torch.cuda.device_count()}")
```

For RAPIDSai:

```python
import cudf

print(cudf.__version__)
```

## More Information

- [RAPIDSai Documentation](https://docs.rapids.ai/)
- [scVI-tools Documentation](https://docs.scvi-tools.org/)
- [PyTorch CUDA Documentation](https://pytorch.org/docs/stable/cuda.html)
