FROM mcr.microsoft.com/devcontainers/python:3.13

COPY requirements-dev.txt /tmp/
COPY docs/requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements-dev.txt && \
    rm -rf /tmp/requirements-dev.txt && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

RUN curl -sSL -o /usr/local/bin/hadolint "https://github.com/hadolint/hadolint/releases/download/v2.14.0/hadolint-Linux-$(dpkg --print-architecture)"
RUN chmod +x /usr/local/bin/hadolint
