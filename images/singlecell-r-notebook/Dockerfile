# Updated Dockerfile

# Section replacing lines 25-27
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git-lfs \
        libcairo2-dev \
        libfreetype6-dev \
        libpng-dev \
        libxml2-dev \
        liblzma-dev \
        libcurl4-openssl-dev \
        libbz2-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        pkg-config \
        build-essential && \
    rm -rf /var/lib/apt/lists/*
# Other content of the Dockerfile follows...
