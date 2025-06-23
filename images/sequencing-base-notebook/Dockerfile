# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=fbnrst
ARG BASE_IMAGE=$REGISTRY/jupyter/datascience-notebook
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

RUN conda config --append channels bioconda

# keeping 'r-base' makes this much faster
RUN mamba install --yes \
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
    'r-base' \
    'r-fastcluster' \
    'r-ggally' \
    'r-ggpubr' \
    # because it contains `mixedsort`
    'r-gtools' \
    'r-languageserver' \
    'r-paletteer' \
    'r-paralleldist' \
    'r-pheatmap' \
    'r-plotly' \
    'r-viridis' \
    'r-writexl' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER ${NB_UID}
