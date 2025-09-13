# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/$OWNER/singlecell-notebook:python-3.12
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
    'napari-spatialdata' \
    'pyproj' \
    'pyqt' \
    'spatial-image' \
    'spatialdata-io' \
    'spatialdata-plot' \
    'spatialdata' \
    'squidpy' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN pip --no-cache-dir install --upgrade \
    spatial-image \
    spatialdata \
    spatialdata-io \
    spatialdata-plot \
    tangram-sc


USER ${NB_UID}
