# Sequencing Jupyter Docker Stacks

[![GitHub Actions Badge](https://github.com/huchlab/sequencing-docker-stacks/actions/workflows/docker.yml/badge.svg)](https://github.com/huchlab/sequencing-docker-stacks/actions/workflows/docker.yml?query=branch%3Amain "Docker image build status")
[![Read the Docs Badge](https://img.shields.io/readthedocs/sequencing-docker-stacks.svg)](https://sequencing-docker-stacks.readthedocs.io/en/latest/ "Documentation build status")
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/huchlab/sequencing-docker-stacks/main.svg)](https://results.pre-commit.ci/latest/github/huchlab/sequencing-docker-stacks/main)
[![Binder Badge](https://static.mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/huchlab/sequencing-docker-stacks/main?urlpath=lab/tree/README.ipynb "Launch a quay.io/jupyter/base-notebook container on mybinder.org")

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

### 🧬 RNA-seq Analysis — `rnaseq-notebook`

**Best for:** Bulk RNA sequencing analysis, differential gene expression, gene set enrichment

**Key Tools:**

- [DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html) — Industry-standard differential expression analysis
- R/Bioconductor ecosystem for statistical analysis
- Data visualization tools (ggplot2, heatmaps, volcano plots)

**Common Use Cases:**

- Compare gene expression between treatment groups
- Identify differentially expressed genes in disease vs. control
- Gene ontology and pathway enrichment analysis
- Quality control and exploratory data analysis of RNA-seq data

### 🔬 Single-Cell Analysis — `singlecell-notebook`

**Best for:** Single-cell RNA-seq (scRNA-seq), cell type identification, trajectory analysis

**Key Tools:**

- [Scanpy](https://scanpy.readthedocs.io/en/stable/) — Python-based single-cell analysis
- [Seurat](https://satijalab.org/seurat/) — R-based single-cell analysis
- Dimensionality reduction (UMAP, t-SNE, PCA)
- Cell clustering and annotation tools

**Common Use Cases:**

- Identify cell populations in heterogeneous samples
- Discover rare cell types
- Trace cell differentiation trajectories
- Integrate multiple single-cell datasets
- Compare cell populations across conditions

### 📍 Spatial Transcriptomics — `spatial-notebook`

**Best for:** Spatial RNA-seq, tissue architecture, spatial patterns

**Key Tools:**

- [Squidpy](https://squidpy.readthedocs.io/en/stable/) — Spatial single-cell analysis
- [SpatialData](https://spatialdata.scverse.org/en/stable/) — Spatial omics data handling
- Spatial statistics and neighborhood analysis
- Image processing capabilities

**Common Use Cases:**

- Analyze gene expression in tissue context
- Identify spatial expression patterns
- Study cell-cell interactions in tissue sections
- Map cellular niches and microenvironments
- Combine imaging and transcriptomics data

### 🧩 Multi-Omics Integration — `multiomics-notebook`

**Best for:** Multi-modal data integration, CITE-seq, ATAC+RNA, multi-assay experiments

**Key Tools:**

- [MOFA2](https://biofam.github.io/MOFA2/) — Multi-Omics Factor Analysis
- [muon](https://github.com/scverse/muon) — Multi-modal omics analysis
- Integration of transcriptomics, epigenomics, and proteomics
- Factor analysis and dimensionality reduction across modalities

**Common Use Cases:**

- Integrate RNA-seq with ATAC-seq data
- Analyze CITE-seq (protein + RNA) experiments
- Discover coordinated patterns across data types
- Multi-modal single-cell analysis
- Systems-level understanding of biological processes

**Not sure which to choose?** Start with the container matching your data type. You can always switch containers later — your notebooks will work across all of them!

## Getting Started

### Prerequisites

1. **Install Docker** on your computer
   - [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
   - [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
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
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/huchlab/singlecell-notebook:latest
```

**What this command does:**

- `docker run` — Start a new container
- `-it` — Interactive mode (you can stop with Ctrl+C)
- `--rm` — Clean up the container when you're done
- `-p 8888:8888` — Access Jupyter at `http://localhost:8888`
- `-v "${PWD}":/home/jovyan/work` — Mount your current directory (your data will be in the `work` folder)
- `quay.io/huchlab/singlecell-notebook:latest` — The container image to use

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
# For RNA-seq analysis
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/huchlab/rnaseq-notebook:latest

# For spatial transcriptomics
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/huchlab/spatial-notebook:latest

# For multi-omics integration
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/huchlab/multiomics-notebook:latest
```

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

### Example Workflows and Tutorials

Check out the [examples](examples) directory for specific use cases and deployment scenarios.

### See What's Installed

Each container comes with dozens of pre-installed tools. For complete lists of installed software and versions, visit the [build manifests in our wiki](https://github.com/huchlab/sequencing-docker-stacks/wiki).

### Find Specific Versions

Images are tagged with dates and commit hashes for reproducibility. To view all available tags for a specific image:

- [rnaseq-notebook tags](https://quay.io/repository/huchlab/rnaseq-notebook?tab=tags)
- [singlecell-notebook tags](https://quay.io/repository/huchlab/singlecell-notebook?tab=tags)
- [spatial-notebook tags](https://quay.io/repository/huchlab/spatial-notebook?tab=tags)
- [multiomics-notebook tags](https://quay.io/repository/huchlab/multiomics-notebook?tab=tags)

**Pro tip:** Use specific tags (like `2024-01-15`) instead of `latest` in your analysis scripts to ensure reproducibility!

## Troubleshooting

### Port Already in Use

If you see "port is already allocated", either:

- Stop other Jupyter instances, or
- Use a different port: `-p 8889:8888` (then access at `http://localhost:8889`)

### Container Won't Start

- Ensure Docker Desktop is running
- Check that you have enough disk space (containers need ~5-10 GB)
- Try pulling the image first: `docker pull quay.io/huchlab/singlecell-notebook:latest`

### Files Not Showing Up

- Make sure you're saving files in the `work` folder inside JupyterLab
- Check that your `-v` mount path is correct
- On Windows, you may need to use absolute paths: `-v C:/Users/YourName/data:/home/jovyan/work`

### Need Help?

- Open an issue on [GitHub](https://github.com/huchlab/sequencing-docker-stacks/issues)
- Check existing issues for common problems
- Provide your Docker version and OS when reporting issues

## Platform Support

- **x86_64** (Intel/AMD processors) — Fully supported
- **aarch64** (ARM/Apple Silicon) — Fully supported

Single-platform images use architecture-specific tags: `quay.io/huchlab/rnaseq-notebook:x86_64-latest`

## About This Project

These containers are built on the [jupyter/docker-stacks](https://github.com/jupyter/docker-stacks) foundation and incorporate tools from the
[Singularity Single Cell container](https://gitlab.hrz.tu-chemnitz.de/dcgc-bfx/singularity/singularity-single-cell).
They are maintained to provide the bioinformatics community with reliable, reproducible analysis environments.

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
