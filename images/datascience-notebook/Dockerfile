# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
ARG REGISTRY=quay.io
ARG OWNER=huchlab
ARG BASE_IMAGE=$REGISTRY/jupyter/datascience-notebook:python-3.13
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

RUN apt-get update && \
    apt-get install -y --no-install-recommends git-lfs && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/R-cran/library && \
    chown "${NB_UID}":"${NB_GID}" /opt/R-cran/library && \
    chmod 775 /opt/R-cran/library

COPY Rprofile.site /opt/conda/lib/R/etc/Rprofile.site

USER ${NB_UID}

RUN git lfs install && \
    conda config --append channels bioconda && \
    echo "r-base >=4.4" >> /opt/conda/conda-meta/pinned && \
    mamba install --yes \
        # Python \
        'jupyterlab_execute_time' \
        'natsort' \
        'openpyxl' \
        'pingouin' \
        'plotnine' \
        'polars' \
        'pyarrow' \
        'scikit-misc' \
        'session-info' \
        'session-info2' \
        'trackhub' \
        'uv' \
        'xlsxwriter' \
        # R \
        'bioconductor-complexheatmap' \
        'r-data.table' \
        'r-dtplyr' \
        'r-fastcluster' \
        'r-feather' \
        'r-ggally' \
        'r-ggpubr' \
        'r-ggrepel' \
        'r-ggsci' \
        'r-ggthemes' \
        'r-gtools' \
        'r-ggvenn' \
        'r-hmisc' \
        'r-janitor' \
        'r-languageserver' \
        'r-openxlsx' \
        'r-paletteer' \
        'r-paralleldist' \
        'r-pheatmap' \
        'r-plotly' \
        'r-r.utils' \
        'r-svglite' \
        'r-viridis' \
        'r-writexl' \
        && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN Rscript -e \
    "Sys.setenv(NOT_CRAN = 'true'); \
    install.packages(c('polars', 'tidypolars'), repos = 'https://community.r-multiverse.org')"
