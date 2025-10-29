# Knowledge Base for Sequencing Docker Stacks

## Image Hierarchy

The images follow a strict dependency hierarchy:

```text
sequencing-base-notebook (base)
├── rnaseq-notebook
├── singlecell-notebook
│   ├── multiomics-notebook
│   └── spatial-notebook
```

## Development Environment

- **VS Code Dev Containers** (`.devcontainer/`): Defines the development environment
  - Base: Python 3.13 from Microsoft's devcontainer images
  - Features: Docker-in-Docker for building images locally
  - Dependencies: Automatically installs from `requirements-dev.txt` using uv
  - Pre-commit: Auto-installs hooks on container creation
  - VS Code Extensions: Pre-configured with GitHub Copilot, Docker, Python tools
- Provides consistent environment across all contributors
- Eliminates "works on my machine" issues
- Recommended setup for repository contributions

## Python Environment

- Base Python version: 3.13
- Package manager: **mamba/conda (preferred)** - must be available for both x86_64 and aarch64
- If package not available via mamba for both architectures, use pip as fallback
- Virtual environment: conda environments within containers
- Jupyter kernels: Python and R (IRkernel)

## R Environment

- R is installed via conda/mamba
- Bioconductor packages are primary focus
- Key packages: DESeq2, Seurat, BiocManager
- **Prefer mamba for R package installation** (check availability for both x86_64 and aarch64)
- Use `install.packages()` or `BiocManager::install()` only when packages are not available via mamba

## Docker Build Process

1. Base image starts from Ubuntu 24.04
2. System dependencies installed via apt
3. Python/conda environment setup
4. Jupyter Lab/Notebook installation
5. Bioinformatics tools installation
6. Configuration and startup scripts

## Testing Strategy

### Test Types

1. **Hierarchy tests**: Verify image inheritance and dependencies
2. **Package tests**: Check installed packages and versions
3. **Import tests**: Automatically test that all mamba-installed packages can be imported
   - Located in `tests/by_image/docker-stacks-foundation/test_packages.py`
   - Tests both Python and R packages
   - Uses `PACKAGE_MAPPING` to map package names to import names
   - When adding packages, update `PACKAGE_MAPPING` if package name differs from import name
   - No new unit test needed for simple package imports
4. **Functionality tests**: Run sample code/notebooks
5. **Integration tests**: Test Jupyter server startup

### Test Execution

- Tests run in Docker containers
- Use pytest fixtures for container management
- Parallel execution supported
- Test images before pushing to registry

## CI/CD Pipeline

### Main Workflows

1. **docker.yml**: Main build, test, and push workflow
2. **docker-build-test-upload.yml**: Build and test specific images
3. **docker-tag-push.yml**: Tag and push images to registry
4. **docker-wiki-update.yml**: Update wiki with build manifests
5. **pre-commit.yml**: Run pre-commit hooks on PRs
6. **sphinx.yml**: Build and deploy documentation

### Registry Management

- Primary registry: quay.io/huchlab
- Mirror to GitLab registry
- Support for multiple architectures (x86_64, aarch64)
- Tag format: `<arch>-<version>` and `latest`

## Common Package Managers

### Conda/Mamba Commands

```bash
mamba install <package>  # Install package
mamba list               # List installed packages
mamba update <package>   # Update package
mamba env list           # List environments
```

### Pip Commands

```bash
pip install <package>    # Install package
pip list                 # List installed packages
pip freeze               # Export requirements
```

## Jupyter Configuration

- Default user: `jovyan`
- Work directory: `/home/jovyan/work`
- Default port: 8888
- Lab by default, notebook available
- Extensions and kernels auto-configured

## Volume Mounting

Typical usage pattern:

```bash
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work <image>
```

- Host directory mounted to `/home/jovyan/work`
- Preserves notebooks and data
- User permissions handled automatically

## Debugging Tips

### Build Issues

1. Check Dockerfile syntax
2. Verify base image availability
3. Check for network issues during package installation
4. Review BuildKit cache

### Test Failures

1. Check container logs
2. Verify package versions
3. Run tests locally with `make test/<image>`
4. Check for architecture-specific issues

### Runtime Issues

1. Check Jupyter server logs
2. Verify kernel installation
3. Check file permissions
4. Verify port mappings

## File Locations in Containers

- Conda/Mamba: `/opt/conda/`
- Jupyter config: `/home/jovyan/.jupyter/`
- User home: `/home/jovyan/`
- Startup scripts: `/usr/local/bin/`
- System libraries: `/usr/lib/`, `/usr/local/lib/`

## Key Dependencies by Image

### rnaseq-notebook

- DESeq2 (R/Bioconductor)
- edgeR, limma
- Gene set enrichment tools
- Visualization packages (ggplot2, etc.)

### singlecell-notebook

- Scanpy (Python)
- Seurat (R)
- scRNA-seq analysis tools
- Visualization tools (UMAP, t-SNE)

### spatial-notebook

- Squidpy (Python)
- SpatialData
- Spatial transcriptomics tools
- Image analysis tools

### multiomics-notebook

- MOFA2 (R)
- muon (Python)
- Integration tools
- Multi-modal analysis packages

## Architecture Support

- x86_64 (amd64): Primary architecture
- aarch64 (arm64): Apple Silicon and ARM servers
- Platform-specific tags when needed
- Multi-arch manifests for convenience

## Documentation

- Built with Sphinx
- Hosted on ReadTheDocs
- Auto-generated from source
- Wiki contains build manifests

## Pre-commit Hooks

Active hooks:

- Black (Python formatting)
- Flake8 (Python linting)
- Hadolint (Dockerfile linting)
- Markdownlint (Markdown linting)
- YAML validation
- Trailing whitespace removal
- End-of-file fixer

## Performance Considerations

- BuildKit caching reduces build times
- Layer optimization in Dockerfiles
- Parallel test execution
- Efficient use of GitHub Actions caching
- Free disk space action for large builds

## Security Updates

- Dependabot monitors GitHub Actions
- Regular base image updates
- Security patches applied promptly
- Vulnerability scanning in CI/CD
