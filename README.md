# Sequencing Jupyter Docker Stacks

[![GitHub Actions Badge](https://github.com/huchlab/sequencing-docker-stacks/actions/workflows/docker.yml/badge.svg)](https://github.com/huchlab/sequencing-docker-stacks/actions/workflows/docker.yml?query=branch%3Amain "Docker image build status")
[![Read the Docs Badge](https://img.shields.io/readthedocs/sequencing-docker-stacks.svg)](https://sequencing-docker-stacks.readthedocs.io/en/latest/ "Documentation build status")
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/huchlab/sequencing-docker-stacks/main.svg)](https://results.pre-commit.ci/latest/github/huchlab/sequencing-docker-stacks/main)
[![Binder Badge](https://static.mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/huchlab/sequencing-docker-stacks/main?urlpath=lab/tree/README.ipynb "Launch a quay.io/jupyter/base-notebook container on mybinder.org")

**Sequencing Docker Stacks** provide ready-to-run [Docker images](https://quay.io/organization/huchlab) tailored for sequencing data analysis.
They are a fork of the [jupyter/docker-stacks](https://github.com/jupyter/docker-stacks) and built upon the [Singularity Single Cell container](https://gitlab.hrz.tu-chemnitz.de/dcgc-bfx/singularity/singularity-single-cell).

## Available Containers

- **`rnaseq-notebook`**: Supports bulk RNA-seq analysis, powered by [DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html).
- **`singlecell-notebook`**: Enables single-cell RNA-seq analysis, incorporating [Scanpy](https://scanpy.readthedocs.io/en/stable/) and [Seurat](https://satijalab.org/seurat/).
  - **`singlecell-notebook:cuda12-*`**: CUDA-enabled variant with GPU acceleration via [RAPIDSai](https://rapids.ai/) and PyTorch CUDA support for [scVI-tools](https://docs.scvi-tools.org/).
- **`spatial-notebook`**: Facilitates spatial transcriptomics, featuring [Squidpy](https://squidpy.readthedocs.io/en/stable/) and [SpatialData](https://spatialdata.scverse.org/en/stable/).
- **`multiomics-notebook`**: Designed for multi-omics analysis, including [MOFA2](https://biofam.github.io/MOFA2/) and [muon](https://github.com/scverse/muon).

Complete build manifests detailing the software stack are available in the [wiki](https://github.com/huchlab/sequencing-docker-stacks/wiki).

## Quick Start

For a smooth start, consider exploring [jupyter/docker-stacks](https://github.com/jupyter/docker-stacks) first.
There, working with Jupyter docker images is explained in detail, including how to run a Jupyter Server and access it via a web browser.

If you [have Docker installed](https://docs.docker.com/get-started/get-docker/), and know which image suits your needs, you can launch a single Jupyter application in a container.

### Example

Run the following command to pull the `singlecell-notebook` image (tagged `latest`) from Quay.io. It starts a container running a Jupyter Server with the JupyterLab frontend, exposing port `8888`:

```bash
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/huchlab/singlecell-notebook:latest
```

## CPU Architectures

- Containers are available for both `x86_64` and `aarch64` platforms.
- Single-platform images use architecture-specific tag prefixes, such as:
  `quay.io/huchlab/rnaseq-notebook:x86_64-latest`

## Development

### GitHub Copilot Integration

This repository includes GitHub Copilot reference configuration to assist contributors with AI-assisted development. The configuration files are located in `.github/copilot/` and provide:

- Repository-specific context and guidelines
- Technical knowledge about the project structure
- Code style and testing preferences
- Common development workflows

These files serve as a reference for contributors using GitHub Copilot or other AI assistants. For more information about the Copilot setup, see [`.github/copilot/README.md`](.github/copilot/README.md).

## LICENSE

This project is licensed under the terms of the Modified BSD License (also known as New or Revised or 3-Clause BSD).
