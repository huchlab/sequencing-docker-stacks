# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
# Modified by Fabian Rost

# https://quay.io/repository/huchlab/singlecell-notebook?tab=tags
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/$OWNER/singlecell-notebook:2025-11-10
FROM $BASE_IMAGE

LABEL maintainer="Fabian Rost <rost@mpi-cbg.de>"

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV TAG="2025-11-10"

COPY --chown=${NB_UID}:${NB_GID} binder/README.ipynb "${HOME}"/README.ipynb

RUN jupyter labextension disable "@jupyterlab/apputils-extension:announcements"
