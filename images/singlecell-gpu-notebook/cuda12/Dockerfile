# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG OWNER=huchlab
ARG BASE_CONTAINER=$OWNER/singlecell-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Huch Lab <huchlab@users.noreply.github.com>"

USER root

# Install rapids-singlecell CPU version via pip
RUN mamba install --yes \
    'rapids=25.10' \
    'cuda-version=12.9' \
    'cudnn' \
    'cutensor' \
    'cusparselt' \
    && \
    uv pip install --system --no-cache-dir \
    'rapids-singlecell' \
    'gdown' \
    'wget' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER ${NB_UID}
