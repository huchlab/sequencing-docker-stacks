# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/$OWNER/spatial-notebook
FROM $BASE_IMAGE

LABEL maintainer="Fabian Rost <rost@mpi-cbg.de>"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]


USER ${NB_UID}

RUN pip install --no-cache-dir \
        'gdown' \
        'rapids-singlecell' \
        'wget' \
    && \
    # Install PyTorch with pip (https://pytorch.org/get-started/locally/)
    # hadolint ignore=DL3013
    pip install --no-cache-dir --index-url 'https://download.pytorch.org/whl/cpu' \
        'torch' \
        'torchaudio' \
        'torchvision' \
    && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
