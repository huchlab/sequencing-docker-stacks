# Sequencing Docker Stacks

[![GitHub Actions Badge](https://github.com/huchlab/sequencing-docker-stacks/actions/workflows/docker.yml/badge.svg)](https://github.com/huchlab/sequencing-docker-stacks/actions/workflows/docker.yml?query=branch%3Amain "Docker image build status")
[![Read the Docs Badge](https://img.shields.io/readthedocs/sequencing-docker-stacks.svg)](https://sequencing-docker-stacks.readthedocs.io/en/latest/ "Documentation build status")
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/huchlab/sequencing-docker-stacks/main.svg)](https://results.pre-commit.ci/latest/github/huchlab/sequencing-docker-stacks/main)
[![Binder Badge](https://static.mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/huchlab/sequencing-docker-stacks/main?urlpath=lab/tree/README.ipynb "Launch a singlecell-notebook container on mybinder.org")

**Ready-to-use analysis environments for your sequencing data** — no installation headaches, just science.

Sequencing Docker Stacks provide pre-configured, reproducible environments for analyzing genomic sequencing data.
Whether you're analyzing RNA-seq, single-cell data, spatial transcriptomics, or multi-omics datasets,
these containers come with all the tools you need already installed and ready to use.

## Who Should Use This?

This project is for you if you:

- **Analyze sequencing data** (RNA-seq, single-cell, spatial transcriptomics, multi-omics)
- **Want a reproducible environment** without manually installing dozens of bioinformatics tools
- **Need to run analysis on different computers** (your laptop, HPC cluster, cloud) with the same setup
- **Collaborate with others** and want everyone using the same software versions
- **Are new to bioinformatics** and overwhelmed by software installation and dependency management

You don't need to be a Docker expert — just follow the Getting Started guide below!

## What's Inside? Choose Your Container

Each container is a complete analysis environment with Jupyter notebooks, Python, R, and specialized bioinformatics tools.
All containers run on both `x86_64` (Intel/AMD) and `aarch64` (ARM/Apple Silicon) architectures.

### Data Science — `data-notebook`

**Best for:** General data science work with Python and R, data visualization, statistical analysis

**Key Tools:**

- Python scientific stack (NumPy, pandas, scikit-learn, matplotlib)
- R with tidyverse and essential packages
- Common data science libraries for both languages
- Jupyter notebook extensions for enhanced productivity

### Sequencing Base — `sequencing-base-notebook`

**Best for:** Foundation for bioinformatics workflows, provides common dependencies for sequencing analysis

**Key Tools:**

- All tools from data-notebook
- Bioinformatics Python packages (biopython, pybiomart)
- R/Bioconductor packages for genomic analysis (DESeq2, fgsea)
- Base layer for specialized sequencing notebooks (RNA-seq, single-cell, etc.)

### RNA-seq Analysis — `rnaseq-notebook`

**Best for:** Bulk RNA sequencing analysis, differential gene expression, gene set enrichment

**Key Tools:**

- [DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html) — differential expression analysis
- R/Bioconductor ecosystem for statistical analysis
- Data visualization tools (ggplot2, heatmaps, volcano plots)

### Single-Cell Analysis — `singlecell-notebook`

**Best for:** Single-cell RNA-seq (scRNA-seq), cell type identification, trajectory analysis

**Key Tools:**

- [Scanpy](https://scanpy.readthedocs.io/en/stable/) — Python-based single-cell analysis
- [Seurat](https://satijalab.org/seurat/) — R-based single-cell analysis
- Dimensionality reduction (UMAP, t-SNE, PCA)
- Cell clustering and annotation tools

### Spatial Transcriptomics — `spatial-notebook`

**Best for:** Spatial RNA-seq, tissue architecture, spatial patterns

**Key Tools:**

- [Squidpy](https://squidpy.readthedocs.io/en/stable/) — Spatial single-cell analysis
- [SpatialData](https://spatialdata.scverse.org/en/stable/) — Spatial omics data handling
- Spatial statistics and neighborhood analysis
- Image processing capabilities

### Multi-Omics Integration — `multiomics-notebook`

**Best for:** Multi-modal data integration, CITE-seq, ATAC+RNA, multi-assay experiments

**Key Tools:**

- [MOFA2](https://biofam.github.io/MOFA2/) — Multi-Omics Factor Analysis
- [muon](https://github.com/scverse/muon) — Multi-modal omics analysis
- Integration of transcriptomics, epigenomics, and proteomics
- Factor analysis and dimensionality reduction across modalities

## Getting Started

### Try Without Installing — Use Binder

**Want to try it first?** You can explore a live notebook environment in your browser without installing anything!

Click the Binder badge at the top of this page or use this link: [![Binder](https://static.mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/huchlab/sequencing-docker-stacks/main?urlpath=lab/tree/README.ipynb)

This will launch a JupyterLab environment running the `singlecell-notebook` container on [mybinder.org](https://mybinder.org).
You'll get a temporary workspace to experiment with single-cell analysis tools like Scanpy and Seurat.

**Note:** Binder sessions are temporary and have limited resources. For real analysis work, follow the installation steps below to run containers on your own computer.

### Prerequisites

1. **Install Docker** on your computer
   - [Docker Desktop for Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
   - [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
   - [Docker Engine for Linux](https://docs.docker.com/engine/install/)

2. **Verify Docker is running**

   ```bash
   docker --version
   ```

   You should see something like `Docker version 20.10.0` or higher.

That's it! No need to install Python, R, or any bioinformatics tools.

### Launch Your First Analysis Environment

Here's how to start a Jupyter notebook environment for single-cell analysis:

```bash
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/huchlab/singlecell-notebook:2025-11-10
```

**What this command does:**

- `docker run` — Start a new container
- `-it` — Interactive mode (you can stop with Ctrl+C)
- `--rm` — Clean up the container when you're done
- `-p 8888:8888` — Access Jupyter at `http://localhost:8888`
- `-v "${PWD}":/home/jovyan/work` — Mount your current directory (your data will be in the `work` folder)
- `quay.io/huchlab/singlecell-notebook:2025-11-10` — The container image to use. Here, `2025-11-10` is the version of the container.
  See [Choose Specific Versions](#choose-specific-versions) below for information on selecting specific image versions.

**After running this command:**

1. Look for a URL in the terminal output that looks like:

   ```text
   http://127.0.0.1:8888/lab?token=abc123...
   ```

2. Copy and paste this URL into your web browser

3. You'll see JupyterLab with all tools pre-installed!

4. Your files from the current directory will be available in the `work` folder

### Choose a Different Container

Replace `singlecell-notebook` with your preferred container:

```bash
# For data science work
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/huchlab/data-notebook:2025-11-10

# For sequencing analysis base (foundation for bioinformatics)
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/huchlab/sequencing-base-notebook:2025-11-10

# For RNA-seq analysis
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/huchlab/rnaseq-notebook:2025-11-10

# For spatial transcriptomics
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/huchlab/spatial-notebook:2025-11-10

# For multi-omics integration
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/huchlab/multiomics-notebook:2025-11-10
```

### Using Apptainer/Singularity Images

For HPC environments that use Apptainer (formerly Singularity) instead of Docker, we provide pre-built Apptainer images on quay.io.
These images have the same tools and configurations as the Docker versions, with `/opt/conda` made writable for all users so you can install additional packages.

**Note:** Apptainer images are currently available for x86_64 architecture only.

Example usage:

```bash
# Run directly without pulling first
apptainer run oras://quay.io/huchlab/singlecell-notebook:2025-11-10-singularity
```

All available images work with Apptainer:

- `rnaseq-notebook`
- `singlecell-notebook`
- `spatial-notebook`
- `multiomics-notebook`
- `sequencing-base-notebook`

Tags follow the pattern: `{date}-singularity` (e.g., `2025-11-10-singularity`)

### Choose Specific Versions

Images are tagged with dates and commit hashes for reproducibility. To view all available tags for a specific image:

- [data-notebook tags](https://quay.io/repository/huchlab/data-notebook?tab=tags)
- [sequencing-base-notebook tags](https://quay.io/repository/huchlab/sequencing-base-notebook?tab=tags)
- [rnaseq-notebook tags](https://quay.io/repository/huchlab/rnaseq-notebook?tab=tags)
- [singlecell-notebook tags](https://quay.io/repository/huchlab/singlecell-notebook?tab=tags)
- [spatial-notebook tags](https://quay.io/repository/huchlab/spatial-notebook?tab=tags)
- [multiomics-notebook tags](https://quay.io/repository/huchlab/multiomics-notebook?tab=tags)

### Alternatives

- [singularity-single-cell](https://gitlab.hrz.tu-chemnitz.de/dcgc-bfx/singularity/singularity-single-cell): singularity-based container for singlecell analysis.
  Usually, R packages are more up-to-date then in our singlecell-notebook
- [scanpy](https://scanpy.readthedocs.io/en/stable/installation.html#docker): [gcfntnu/scanpy](https://hub.docker.com/r/gcfntnu/scanpy) image on Docker Hub
- [scvi-tools](https://docs.scvi-tools.org/en/stable/installation.html#docker) from the scverse provides Docker images
- [Seurat](https://satijalab.org/seurat/articles/install.html#docker) provides Docker images

### Working With Your Data

**Important:** Any files you want to keep must be saved in the `work` folder inside Jupyter.
This folder is connected to your computer's current directory, so files saved here persist after the container stops.

Files saved elsewhere in the container will be lost when the container stops!

## Next Steps

### Learn More About Jupyter and Docker

If you're new to Jupyter or Docker containers, we recommend exploring the [jupyter/docker-stacks](https://github.com/jupyter/docker-stacks) documentation for detailed explanations of:

- How Jupyter servers work
- Advanced Docker options (resource limits, environment variables)
- Running containers in different environments (cloud, HPC)
- Security best practices

### See What's Installed

Each container comes with dozens of pre-installed tools. For complete lists of installed software and versions, visit the [build manifests in our wiki](https://github.com/huchlab/sequencing-docker-stacks/wiki).

## Need Help?

- Open an issue on [GitHub](https://github.com/huchlab/sequencing-docker-stacks/issues)
- Check existing issues for common problems
- Provide your Docker version and OS when reporting issues

## About This Project

These containers are built on the [jupyter/docker-stacks](https://github.com/jupyter/docker-stacks) foundation and incorporates experience from the
[Singularity Single Cell container](https://gitlab.hrz.tu-chemnitz.de/dcgc-bfx/singularity/singularity-single-cell).

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huchlab/sequencing-docker-stacks&type=Date)](https://star-history.com/#huchlab/sequencing-docker-stacks&Date)

## Development

### GitHub Copilot Integration

This repository includes GitHub Copilot reference configuration to assist contributors with AI-assisted development. The configuration files are located in `.github/copilot/` and provide:

- Repository-specific context and guidelines
- Technical knowledge about the project structure
- Code style and testing preferences
- Common development workflows

These files serve as a reference for contributors using GitHub Copilot or other AI assistants. For more information about the Copilot setup, see [`.github/copilot/README.md`](https://github.com/huchlab/sequencing-docker-stacks/blob/main/.github/copilot/README.md).

## LICENSE

This project is licensed under the terms of the Modified BSD License (also known as New or Revised or 3-Clause BSD).
