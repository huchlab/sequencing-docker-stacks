# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=fbnrst
ARG BASE_IMAGE=$REGISTRY/$OWNER/sequencing-base-notebook
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

ARG GITHUB_TOKEN
ENV GITHUB_PAT=$GITHUB_TOKEN

USER ${NB_UID}

RUN mamba install --yes \
    # Python
    'anndata' \
    'anndata2ri' \
    'arboreto' \
    'bbknn' \
    'cellrank>=2.0' \
    'celltypist' \
    'decoupler-py' \
    'harmonypy' \ 
    # optional dependency of scvelo
    'hnswlib' \ 
    'leidenalg' \
    # fixed #40
    'lightning>=2.5' \
    'loompy' \
    'louvain' \
    'mudata' \
    'muon' \
    'palantir' \
    # optional dependency of scvelo 
    'pybind11' \ 
    'pydeseq2>=0.5.0' \
    'python-igraph' \
    'scanorama' \
    'scanpy>=1.10.4' \
    'scrublet' \
    'scvelo' \
    'scvi-tools>=1.2.2' \
    # R
    'bioconductor-loomexperiment' \
    'bioconductor-mast' \
    'bioconductor-milor' \
    'bioconductor-monocle' \
    'bioconductor-scater' \
    'bioconductor-scran' \
    'bioconductor-singlecellexperiment' \
    'r-data.table' \
    'r-reticulate' \
    'r-seurat>=5.1.0' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER root

RUN chmod a+w /opt/conda/

USER ${NB_UID}

# packages not available for arm64 on conda 
RUN pip install --no-cache-dir \
    fastcluster \
    liana \
    scikit-misc

# do not install dependencies for cellbender (they include jupyter)
RUN pip install --no-cache-dir --no-deps \
    cellbender 

RUN R -e "devtools::install_github('cellgeni/sceasy', threads = 4)"