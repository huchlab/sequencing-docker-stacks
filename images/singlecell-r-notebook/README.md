# Jupyter Notebook Single-Cell R Stack

This image provides an optimized single-cell analysis environment with the most recent R packages directly from Bioconductor.

Unlike the standard `singlecell-notebook` which is built on the data stack and uses the bioconda channel (which typically lags behind Bioconductor releases), this image is built directly on `jupyter/datascience-notebook` to ensure access to the latest R package versions from Bioconductor.

## Key Differences from singlecell-notebook

- **R Version**: Pinned to r-base>=4.5 for latest R features
- **Package Sources**: R packages are installed directly from Bioconductor rather than bioconda
- **Base Image**: Built directly on jupyter/datascience-notebook instead of the data-notebook stack
- **Purpose**: Optimized for R-centric single-cell workflows requiring the latest R package versions

## Included Tools

This image combines all dependencies from:

- `data-notebook`: General data science tools
- `sequencing-base-notebook`: Core bioinformatics packages
- `singlecell-notebook`: Single-cell analysis tools (both Python and R)

With focus on R package currency from Bioconductor.

GitHub Actions in the <https://github.com/huchlab/sequencing-docker-stacks> project builds and pushes this image to the Registry.

Please visit the [project site](https://github.com/huchlab/sequencing-docker-stacks) for help to use and contribute to this image and others.
