FROM mcr.microsoft.com/devcontainers/python:3.13

COPY requirements-dev.txt /tmp/
RUN pip3 install --no-cache-dir uv && \
    uv pip install --system --no-cache-dir -r /tmp/requirements-dev.txt && \
    rm -rf /tmp/requirements-dev.txt
