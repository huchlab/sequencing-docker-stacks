# Jupyter Notebook Spatial GPU Stack

GitHub Actions in the <https://github.com/huchlab/sequencing-docker-stacks> project builds and pushes this image to the Registry.

Please visit the [project site](https://github.com/huchlab/sequencing-docker-stacks) for help to use and contribute to this image and others.

## Image Features

This image extends `spatial-notebook` with GPU-acceleration from [rapids-singlecell](https://rapids-singlecell.readthedocs.io/)

## Variants

### Default Variant

The default variant installs `rapids-singlecell` without CUDA dependencies. This merely serves as a base for the CUDA variant.

### CUDA 13 Variant (`cuda13`)

The `cuda13` variant includes NVIDIA CUDA 13 support with:

- **RAPIDS 25.12**: Full GPU-accelerated data science suite
- **cuML**: GPU-accelerated machine learning algorithms
- **CUDA 13.x**: Latest CUDA toolkit
- **cuDNN, cuTensor, cuSPARSELt**: Optimized GPU libraries

**Note**: The CUDA variant requires an NVIDIA GPU and appropriate drivers on the host system. Use `--gpus all` flag when running the container:

```bash
docker run --gpus all -p 8888:8888 quay.io/huchlab/spatial-gpu-notebook:cuda13-latest
```
