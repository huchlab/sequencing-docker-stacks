FROM mcr.microsoft.com/devcontainers/python:3.12

COPY requirements-dev.txt /tmp/
RUN pip3 install --no-cache-dir uv && \
    uv pip install --system --no-cache-dir -r /tmp/requirements-dev.txt && \
    rm -rf /tmp/requirements-dev.txt

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
