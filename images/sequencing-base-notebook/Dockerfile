# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/jupyter/datascience-notebook:python-3.12
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
    apt-get install -y --no-install-recommends git-lfs && \
    rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

RUN git lfs install && \
    conda config --append channels bioconda && \
    mamba install --yes \
    # Python \
    'biopython' \
    'gseapy' \
    'jupyterlab_execute_time' \
    'natsort' \
    'plotnine' \
    'pybiomart' \
    'openpyxl' \
    'session-info' \
    # R \
    'bioconductor-complexheatmap' \
    'bioconductor-deseq2' \
    'bioconductor-fgsea' \
    # keeping 'r-base' makes this much faster
    'r-base' \
    'r-fastcluster' \
    'r-ggally' \
    'r-ggpubr' \
    'r-ggvenn' \
    'r-languageserver' \
    'r-paletteer' \
    'r-paralleldist' \
    'r-pheatmap' \
    'r-plotly' \
    # because it contains `mixedsort`
    'r-gtools' \
    'r-viridis' \
    'r-writexl' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER ${NB_UID}
