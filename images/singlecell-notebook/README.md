# Jupyter Notebook Singlecell Stack

GitHub Actions in the <https://github.com/huchlab/sequencing-docker-stacks> project builds and pushes this image to the Registry.

Please visit the [project site](https://github.com/huchlab/sequencing-docker-stacks) for help to use and contribute to this image and others.

## CUDA Variant

A CUDA-enabled variant of this image is available with GPU acceleration support:

- **`singlecell-notebook:cuda12-*`**: Includes CUDA 12.8 support with RAPIDSai libraries (cuDF, cuML, cuGraph) for GPU-accelerated data science operations and scVI-tools with PyTorch CUDA backend for GPU-accelerated variational inference.

### Usage

To use the CUDA variant, ensure you have:
1. NVIDIA GPU with CUDA support
2. NVIDIA Container Toolkit installed
3. Run with GPU access: `docker run --gpus all -it --rm -p 8888:8888 quay.io/huchlab/singlecell-notebook:cuda12-latest`

### Features

The CUDA variant includes all packages from the base singlecell-notebook plus:
- **RAPIDSai**: GPU-accelerated libraries for data science (cuDF, cuML, cuGraph)
- **PyTorch with CUDA**: GPU-enabled deep learning framework
- **scVI-tools with CUDA**: GPU-accelerated single-cell variational inference

