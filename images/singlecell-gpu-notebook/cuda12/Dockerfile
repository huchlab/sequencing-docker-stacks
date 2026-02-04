# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/$OWNER/singlecell-notebook
FROM $BASE_IMAGE

LABEL maintainer="Fabian Rost <rost@mpi-cbg.de>"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

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
    -c rapidsai \
    -c nvidia \
        'cudnn' \
        'cusparselt' \
        'cuda-version=12.9' \
        'cutensor' \
        'rapids=25.12' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN pip install --no-cache-dir \
        'gdown' \
        'rapids-singlecell' \
        'wget' \
    && \
    # Install PyTorch with pip (https://pytorch.org/get-started/locally/)
    # hadolint ignore=DL3013
    pip install --no-cache-dir --extra-index-url=https://pypi.nvidia.com --index-url 'https://download.pytorch.org/whl/cu129' \
        'torch' \
        'torchaudio' \
        'torchvision' \
    && \
    pip install --no-cache-dir \
        'scvi-tools[cuda]' \
    && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# CUDA environment variables
ENV NVIDIA_VISIBLE_DEVICES="all" \
    NVIDIA_DRIVER_CAPABILITIES="compute,utility"

# Puts the nvidia-smi binary (system management interface) on path
# with associated library files to execute it
ENV PATH="${PATH}:/usr/local/nvidia/bin" \
    LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/local/nvidia/lib64"
