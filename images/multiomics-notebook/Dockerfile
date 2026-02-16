# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/$OWNER/singlecell-notebook
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
    'mofapy2' \
    'muon' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN Rscript -e "BiocManager::install('MOFA2', ask = FALSE)"

USER ${NB_UID}
