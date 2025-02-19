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

USER ${NB_UID}

RUN conda config --add channels bioconda

RUN mamba install --yes \
    # Python \
    'anndata' \
    'anndata2ri' \
    'arboreto' \
    'bbknn' \
    'celltypist' \
    'decoupler-py' \
    'gseapy' \
    'harmonypy' \ 
    'leidenalg' \
    'loompy' \
    'louvain' \
    'mscorefonts' \
    'mudata' \
    'muon' \
    'openpyxl' \
    'pybiomart' \
    'python-igraph' \
    'scanorama' \
    'scanpy>=1.10.4' \
    'scrublet' \
    'scvi-tools>=1.2.2' \
    'session-info' \
    # R \
    'bioconductor-singlecellexperiment' \
    'bioconductor-monocle' \
    'bioconductor-mast' \
    'bioconductor-scater' \
    'bioconductor-scran' \
    'r-seurat>=5.1.0' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN pip install --no-cache-dir fastcluster

# import decoupler to combile numba
RUN python -c "import decoupler"