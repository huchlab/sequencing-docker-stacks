# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/$OWNER/data-notebook
FROM $BASE_IMAGE

LABEL maintainer="Fabian Rost <rost@mpi-cbg.de>"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

ARG CONTAINER_BUILD_DATE
ARG CONTAINER_IMAGE_NAME
ARG CONTAINER_GIT_REPOSITORY
ARG CONTAINER_GIT_COMMIT

LABEL org.opencontainers.image.created="${CONTAINER_BUILD_DATE}" \
      org.opencontainers.image.title="${CONTAINER_IMAGE_NAME}" \
      org.opencontainers.image.source="${CONTAINER_GIT_REPOSITORY}" \
      org.opencontainers.image.revision="${CONTAINER_GIT_COMMIT}"

USER ${NB_UID}

RUN mamba install --yes \
    # Python \
    'biopython' \
    # 'gseapy' \
    'pybiomart' \
    # R \
    'bioconductor-deseq2' \
    'bioconductor-dose' \
    'bioconductor-fgsea' \
    'bioconductor-org.hs.eg.db' \
    'bioconductor-org.mm.eg.db' \
    'bioconductor-topgo' \
    'bioconductor-trackviewer' \
    # keeping 'r-base' makes this much faster
    'r-base' \
    'r-biocmanager' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN pip install --no-cache-dir \
    gseapy && \
    # Install R packages not available for arm64 on conda
    Rscript -e "install.packages('openxlsx2')"
