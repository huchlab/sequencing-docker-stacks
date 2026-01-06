# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/huchlab/datascience-notebook:latest
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
    echo "r-base >=4.4" >> /opt/conda/conda-meta/pinned && \
    mamba install --yes \
    # Python \
    'biopython' \
    # 'gseapy' \
    'jupyterlab_execute_time' \
    'natsort' \
    'plotnine' \
    'pybiomart' \
    'openpyxl' \
    'session-info' \
    'session-info2' \
    'uv' \
    # R \
    'bioconductor-complexheatmap' \
    'bioconductor-deseq2' \
    'bioconductor-fgsea' \
    'bioconductor-trackviewer' \
    # keeping 'r-base' makes this much faster
    'r-base' \
    'r-biocmanager' \
    'r-fastcluster' \
    'r-ggally' \
    'r-ggpubr' \
    # because it contains `mixedsort`
    'r-gtools' \
    'r-ggvenn' \
    'r-janitor' \
    'r-languageserver' \
    'r-openxlsx' \
    'r-paletteer' \
    'r-paralleldist' \
    'r-pheatmap' \
    'r-plotly' \
    'r-svglite' \
    'r-viridis' \
    'r-writexl' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN pip install --no-cache-dir \
    gseapy && \
    # Install R packages not available for arm64 on conda
    R -e "install.packages('openxlsx2', repos = 'https://cloud.r-project.org/', Ncpus = 4)"

USER ${NB_UID}
