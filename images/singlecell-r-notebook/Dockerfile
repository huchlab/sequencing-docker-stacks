# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/jupyter/datascience-notebook:python-3.13
FROM $BASE_IMAGE

LABEL maintainer="Fabian Rost <rost@mpi-cbg.de>"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

ARG CONTAINER_BUILD_DATE
ARG CONTAINER_IMAGE_NAME
ARG CONTAINER_GIT_REPOSITORY
ARG CONTAINER_GIT_COMMIT

ENV CONTAINER_BUILD_DATE=${CONTAINER_BUILD_DATE}
ENV CONTAINER_IMAGE_NAME=$CONTAINER_IMAGE_NAME
ENV CONTAINER_GIT_REPOSITORY=$CONTAINER_GIT_REPOSITORY
ENV CONTAINER_GIT_COMMIT=$CONTAINER_GIT_COMMIT

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git-lfs && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/R-cran/library && \
    chown "${NB_UID}":"${NB_GID}" /opt/R-cran/library && \
    chmod 775 /opt/R-cran/library

COPY Rprofile.site /opt/conda/lib/R/etc/Rprofile.site
RUN chown "${NB_UID}":"${NB_GID}" /opt/conda/lib/R/etc/Rprofile.site && \
    chmod 775 /opt/conda/lib/R/etc/Rprofile.site

ENV RETICULATE_PYTHON="/opt/conda/bin/python"

USER ${NB_UID}

RUN git lfs install && \
    conda config --append channels bioconda && \
    echo "r-base >=4.5" >> /opt/conda/conda-meta/pinned && \
    mamba install --yes \
        # Python packages (alphabetically sorted) \
        'anndata' \
        'anndata2ri' \
        'arboreto' \
        'biopython' \
        'cellrank>=2.0' \
        'celltypist' \
        'decoupler-py>=2.0.2' \
        'harmonypy>=0.2.0' \
        'hnswlib' \
        'jupyterlab_execute_time' \
        'leidenalg' \
        'lightning>=2.5' \
        'loompy' \
        'marsilea' \
        'mudata' \
        'muon' \
        'natsort' \
        'openpyxl' \
        'palantir' \
        'pingouin' \
        'plotnine' \
        'polars' \
        'pooch' \
        'pyarrow' \
        'pybind11' \
        'pybiomart' \
        'pydeseq2>=0.5.0' \
        'python-igraph' \
        'scanorama' \
        'scanpy>=1.10.4' \
        'scikit-misc' \
        'scrublet' \
        'scvelo' \
        'scvi-tools>=1.2.2' \
        'session-info' \
        'session-info2' \
        'trackhub' \
        'uv' \
        'xlsxwriter' \
        # R packages (alphabetically sorted, non-Bioconductor) \
        # 'r-anndata' \
        'r-base' \
        'r-biocmanager' \
        'r-clustree' \
        'r-data.table' \
        'r-dtplyr' \
        'r-fastcluster' \
        'r-feather' \
        'r-ggally' \
        'r-ggpubr' \
        'r-ggrepel' \
        'r-ggsci' \
        'r-ggthemes' \
        'r-gtools' \
        'r-ggvenn' \
        'r-harmony' \
        'r-hmisc' \
        'r-janitor' \
        'r-languageserver' \
        'r-openxlsx' \
        'r-paletteer' \
        'r-paralleldist' \
        'r-pheatmap' \
        'r-plotly' \
        # 'r-presto' \
        'r-r.utils' \
        'r-remotes' \
        'r-reticulate' \
        'r-seurat>=5.1.0' \
        'r-svglite' \
        'r-viridis' \
        'r-writexl' \
        # next packages are deps for bioconductor packages below
        'r-cairo' \
        'r-gdtools' \
        'r-ggrastr' \
        'r-locfit' \
        'xz' \
        && \
    # workaround to fix #486
    mamba install r-zoo r-tseries --yes --force-reinstall && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Packages not available for one or both architectures on conda
RUN pip install --no-cache-dir \
    'gseapy' \
    'cytetype' \
    'fa2_modified' \
    'fastcluster' \
    'liana>=1.6.1' \
    'omnipath>=1.0.12' \
    'scikit-misc' \
    'vitessce[all]' \
    && \
    # do not install dependencies for cellbender (they include jupyter)
    pip install --no-cache-dir --no-deps cellbender

# Install R packages not available for arm64 on conda
RUN --mount=type=secret,id=GITHUB_PAT,env=GITHUB_PAT \
    Rscript -e "install.packages('anndata')" && \
    Rscript -e "install.packages('openxlsx2')" && \
    Rscript -e "install.packages('scCustomize')" && \
    Rscript -e "remotes::install_github('cellgeni/sceasy', upgrade = FALSE)" && \
    Rscript -e "remotes::install_github('immunogenomics/presto', upgrade = FALSE)"

# Install Bioconductor packages using BiocManager for R 4.5 compatibility
RUN Rscript -e "options(warn = 2); BiocManager::install(c( \
        'anndataR', \
        'batchelor', \
        'clusterProfiler', \
        'ComplexHeatmap', \
        'DESeq2', \
        'fgsea', \
        'LoomExperiment', \
        'MAST', \
        'miloR', \
        'Nebulosa', \
        # rhdf5 is optional dependency of anndataR
        'rhdf5', \
        'scater', \
        'scran', \
        'SingleCellExperiment', \
        'trackViewer', \
        'zellkonverter' \
    ), ask = FALSE, update = FALSE)" && \
    # Install CellChat afterwards, because it depends on ComplexHeatmap
    # recent NMF is a dependency of CellChat
    Rscript -e "install.packages('NMF')" && \
    Rscript -e "remotes::install_github('jinworks/CellChat', upgrade = FALSE)"

USER ${NB_UID}
