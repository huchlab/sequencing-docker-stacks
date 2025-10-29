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

ENV CONTAINER_BUILD_DATE=${CONTAINER_BUILD_DATE}
ENV CONTAINER_IMAGE_NAME=$CONTAINER_IMAGE_NAME
ENV CONTAINER_GIT_REPOSITORY=$CONTAINER_GIT_REPOSITORY
ENV CONTAINER_GIT_COMMIT=$CONTAINER_GIT_COMMIT

# https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html#dockerfiles
ENV NVIDIA_VISIBLE_DEVICES="all" \
    NVIDIA_DRIVER_CAPABILITIES="compute,utility"

# Puts the nvidia-smi binary (system management interface) on path
# with associated library files to execute it
ENV PATH="${PATH}:/usr/local/nvidia/bin" \
    LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/local/nvidia/lib64"

USER ${NB_UID}

# Install PyTorch with CUDA support
# https://pytorch.org/get-started/locally/
RUN uv pip install --system --no-cache-dir --extra-index-url=https://pypi.nvidia.com --index-url 'https://download.pytorch.org/whl/cu121' \
    'torch' \
    'torchvision' \
    'torchaudio' && \
    # Reinstall scvi-tools to ensure it uses CUDA-enabled PyTorch
    uv pip install --system --no-cache-dir --force-reinstall --no-deps \
    'scvi-tools>=1.2.2'

# Install RAPIDSai libraries for GPU-accelerated data science
# https://docs.rapids.ai/install
# Note: Installing core RAPIDS components that are available
RUN mamba install --yes -c rapidsai -c conda-forge -c nvidia \
    'cudf-cu12' \
    'cuml-cu12' \
    'cugraph-cu12' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER ${NB_UID}
