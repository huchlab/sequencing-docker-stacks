# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG OWNER=huchlab
ARG BASE_CONTAINER=$OWNER/singlecell-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Huch Lab <huchlab@users.noreply.github.com>"

USER root

# Install rapids-singlecell CPU version via pip
RUN uv pip install --system --no-cache-dir \
    'rapids-singlecell' \
    'gdown' \
    'wget'

USER ${NB_UID}

WORKDIR "${HOME}"
