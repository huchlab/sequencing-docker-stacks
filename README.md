# Sequencing Jupyter Docker Stacks

[![GitHub actions badge](https://github.com/fbnrst/sequencing-docker-stacks/actions/workflows/docker.yml/badge.svg)](https://github.com/fbnrst/sequencing-docker-stacks/actions/workflows/docker.yml?query=branch%3Amain "Docker images build status")


Sequencing Docker Stacks are a set of ready-to-run [Docker images](https://quay.io/organization/fbnrst) containing sequencing data analysis tools. They are based on the [jupyter/docker-stacks](https://github.com/jupyter/docker-stacks) and the [singularity single cell container](https://gitlab.hrz.tu-chemnitz.de/dcgc-bfx/singularity/singularity-single-cell).

## Quick Start

Make sure to try [jupyter/docker-stacks](https://github.com/jupyter/docker-stacks) first.
<!-- You can [try a relatively recent build of the quay.io/jupyter/base-notebook image on mybinder.org](https://mybinder.org/v2/gh/fbnrst/sequencing-docker-stacks/main?urlpath=lab/tree/README.ipynb). -->
The examples below may help you get started if you [have Docker installed](https://docs.docker.com/get-started/get-docker/),
know which Docker image you want to use, and want to launch a single Jupyter Application in a container.

### Example 

This command pulls the `rnaseq-notebook` image tagged `latest` from Quay.io if it is not already present on the local host.
It then starts a container running a Jupyter Server with the JupyterLab frontend and exposes the container's internal port `8888` to port `10000` of the host machine:

```bash
docker run -it --rm  -p 10000:8888 quay.io/fbnrst/rnaseq-notebook:latest
```

## CPU Architectures

- We publish containers for both `x86_64` and `aarch64` platforms
- Single-platform images have either `aarch64-` or `x86_64-` tag prefixes, for example, `quay.io/jupyter/base-notebook:aarch64-python-3.11.6`

## License

This container image is licensed under the BSD 3-Clause License.  
It based on the [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io), which are licensed under the BSD 3-Clause License.
