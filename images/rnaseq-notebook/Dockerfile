# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/$OWNER/sequencing-base-notebook
FROM $BASE_IMAGE

LABEL maintainer="Fabian Rost <rost@mpi-cbg.de>"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root


USER ${NB_UID}

# keeping 'r-base' makes this much faster
RUN mamba install --yes \
    'bioconductor-apeglm' \
    'bioconductor-biocparallel' \
    'bioconductor-biomart' \
    'bioconductor-clusterprofiler' \
    'bioconductor-glmgampoi' \
    'bioconductor-gseabase' \
    'bioconductor-gsva' \
    'bioconductor-gviz' \
    'bioconductor-reactomepa' \
    'bioconductor-scuttle' \
    'bioconductor-sva' \
    'bioconductor-tximeta' \
    'bioconductor-tximport' \
    'bioconductor-variancepartition' \
    'bioconductor-vsn' \
    'r-ashr' \
    'r-base' \
    'r-dendextend' \
    'r-magick' \
    'r-robustrankaggreg' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER ${NB_UID}
