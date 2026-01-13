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

ARG CONTAINER_BUILD_DATE
ARG CONTAINER_IMAGE_NAME
ARG CONTAINER_GIT_REPOSITORY
ARG CONTAINER_GIT_COMMIT

ENV CONTAINER_BUILD_DATE=${CONTAINER_BUILD_DATE}
ENV CONTAINER_IMAGE_NAME=$CONTAINER_IMAGE_NAME
ENV CONTAINER_GIT_REPOSITORY=$CONTAINER_GIT_REPOSITORY
ENV CONTAINER_GIT_COMMIT=$CONTAINER_GIT_COMMIT

ENV RETICULATE_PYTHON="/opt/conda/bin/python"

USER ${NB_UID}

RUN mamba install --yes \
    # Python
    'anndata' \
    'anndata2ri' \
    'arboreto' \
    'cellrank>=2.0' \
    'celltypist' \
    'decoupler-py>=2.0.2' \
    'harmonypy' \
    # optional dependency of scvelo
    'hnswlib' \
    'leidenalg' \
    # fixed #40
    'lightning>=2.5' \
    'loompy' \
    'marsilea' \
    'mudata' \
    'muon' \
    'palantir' \
    'pooch' \
    # optional dependency of scvelo
    'pybind11' \
    'pydeseq2>=0.5.0' \
    'python-igraph' \
    'scanorama' \
    'scanpy>=1.10.4' \
    'scrublet' \
    'scvelo' \
    'scvi-tools>=1.2.2' \
    # R
    'r-ashr' \
    'r-base' \
    'r-dendextend' \
    'r-magick' \
    'r-robustrankaggreg' \
    && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN Rscript -e "\
    BiocManager::install(c( \
        'apeglm', \
        'BiocParallel', \
        'biomaRt', \
        'clusterProfiler', \
        'GLMGamPoi', \
        'GSEABase', \
        'GSVA', \
        'Gviz', \
        'org.Hs.eg.db', \
        'org.Mm.eg.db', \
        'ReactomePA', \
        'scuttle', \
        'sva', \
        'tximeta', \
        'tximport', \
        'variancePartition', \
        'vsn' \
    ), ask = FALSE, update = FALSE, Ncpus = 4); \
    stopifnot(require(apeglm), require(BiocParallel), require(biomaRt), require(clusterProfiler), require(glmGamPoi), require(GSEABase), require(GSVA), require(Gviz), require(org.Hs.eg.db), require(org.Mm.eg.db), require(ReactomePA), require(scuttle), require(sva), require(tximeta), require(tximport), require(variancePartition), require(vsn))\
    "

# packages not available for one or both architectures on conda
RUN pip install --no-cache-dir \
    cytetype \
    fa2_modified \
    fastcluster \
    "liana>=1.6.1" \
    "omnipath>=1.0.12" \
    scikit-misc \
    "vitessce[all]" \
    && \
    # do not install dependencies for cellbender (they include jupyter)
    pip install --no-cache-dir --no-deps cellbender

RUN --mount=type=secret,id=GITHUB_PAT,env=GITHUB_PAT \
    R -e "options(warn = 2); BiocManager::install('miloR', Ncpus = 4, ask = FALSE, update = FALSE)" && \
    R -e "install.packages('scCustomize', repos = 'https://cloud.r-project.org/', Ncpus = 4)" && \
    R -e "remotes::install_github('jinworks/CellChat', Ncpus = 4, upgrade = FALSE)" && \
    R -e "remotes::install_github('cellgeni/sceasy', Ncpus = 4, upgrade = FALSE)"

USER ${NB_UID}
