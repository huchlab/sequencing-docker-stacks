# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/$OWNER/datascience-notebook
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

RUN mamba install --yes \
    # Python \
    'biopython' \
    # 'gseapy' \
    'pybiomart' \
    # R \
    # keeping 'r-base' makes this much faster
    'r-base' \
    'r-biocmanager' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN Rscript -e "\
    BiocManager::install(c( \
        'DESeq2', \
        'fgsea', \
        'trackViewer' \
    ), ask = FALSE, update = FALSE, Ncpus = 4)\
    "

RUN pip install --no-cache-dir \
    gseapy && \
    # Install R packages not available for arm64 on conda
    R -e "install.packages('openxlsx2', repos = 'https://cloud.r-project.org/', Ncpus = 4)"
