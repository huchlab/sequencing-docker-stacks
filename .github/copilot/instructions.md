# Copilot Instructions for Sequencing Docker Stacks

## Repository Overview

This repository provides **Sequencing Docker Stacks** - ready-to-run Docker images tailored for sequencing data analysis. The images are based on the
[jupyter/docker-stacks](https://github.com/jupyter/docker-stacks) and built upon the Singularity Single Cell container.

## Available Containers

- **rnaseq-notebook**: Bulk RNA-seq analysis (DESeq2)
- **singlecell-notebook**: Single-cell RNA-seq analysis (Scanpy, Seurat)
- **spatial-notebook**: Spatial transcriptomics (Squidpy, SpatialData)
- **multiomics-notebook**: Multi-omics analysis (MOFA2, muon)
- **sequencing-base-notebook**: Base image with common dependencies

## Key Technologies

- Docker and Docker BuildKit
- Python 3.13
- Jupyter Notebook/Lab
- Bioconductor (R packages)
- Various bioinformatics tools (Scanpy, Seurat, DESeq2, etc.)
- Pytest for testing
- Sphinx for documentation
- Pre-commit hooks for code quality

## Repository Structure

- `/images/`: Dockerfiles and configuration for each image
- `/tests/`: Pytest tests organized by image and shared checks
- `/docs/`: Sphinx documentation
- `/tagging/`: Scripts for image tagging and manifest generation
- `/examples/`: Example notebooks demonstrating usage
- `.github/workflows/`: CI/CD workflows for building and testing
- `.github/actions/`: Reusable GitHub Actions
- `.devcontainer/`: Development environment configuration for VS Code Dev Containers

## Development Guidelines

### Code Style

- Follow existing code conventions
- **Always run and fix pre-commit hooks before committing** (configured in `.pre-commit-config.yaml`)
- Python code should follow PEP 8 (enforced by flake8)
- Python imports should be properly sorted (enforced by isort with black profile)
- Dockerfiles should follow best practices (checked by hadolint)
- Markdown should follow markdownlint rules (max line length: 200 characters)
- **Before finalizing any PR, ensure all linting checks pass:**
  - `flake8` for Python code quality
  - `isort` for import ordering
  - `black` for Python code formatting
  - `hadolint` for Dockerfile linting
  - `markdownlint-cli2` for Markdown formatting

### Development Environment

- **`.devcontainer/`**: Defines the development environment for VS Code Dev Containers
  - Uses Python 3.13 base image from Microsoft
  - Installs development dependencies from `requirements-dev.txt`
  - Includes Docker-in-Docker feature for building images
  - Pre-configures VS Code extensions (GitHub Copilot, Docker, Python, etc.)
  - Auto-installs pre-commit hooks on container creation
- Provides consistent development setup across contributors
- Recommended for contributing to this repository

### Docker Images

- All images inherit from a base image in dependency order
- Use BuildKit for builds (`DOCKER_BUILDKIT=1`)
- Images support both x86_64 and aarch64 architectures
- Tag structure: `quay.io/huchlab/<image-name>:<tag>`

### Testing

- Run tests with `make test/<image-name>`
- Tests are organized by image in `tests/by_image/`
- Shared tests are in `tests/shared_checks/`
- All tests use pytest framework
- **Import tests**: Automatically test that all mamba-installed packages can be imported
  - Located in `tests/by_image/docker-stacks-foundation/test_packages.py`
  - Uses `PACKAGE_MAPPING` dictionary to map package names to import names
  - When adding new packages, update `PACKAGE_MAPPING` if package name differs from import name
  - No new unit test needed for simple package imports

### Building

- Build specific image: `make build/<image-name>`
- Build all images: `make build-all`
- Clean containers: `make cont-clean-all`
- Remove images: `make img-rm`

### Documentation

- Build docs: `make docs`
- Check links: `make linkcheck-docs`
- Documentation uses Sphinx and reStructuredText
- Update documentation for significant changes

### Commits and Pull Requests

- Follow the PR template in `.github/pull_request_template.md`
- Include self-review checklist
- Add thorough tests for core features
- Update documentation for significant changes
- Use conventional commit messages

## Important Files

- `Makefile`: Main build and test automation
- `.pre-commit-config.yaml`: Pre-commit hook configuration
- `pytest.ini`: Pytest configuration
- `requirements-dev.txt`: Development dependencies
- `.devcontainer/`: Development environment configuration (Python 3.13, dev tools, VS Code extensions)
- `.flake8`: Python linting configuration
- `.hadolint.yaml`: Dockerfile linting configuration
- `.markdownlint.yaml`: Markdown linting configuration

## Common Tasks

### Adding a New Image

1. Create directory in `/images/<new-image-name>/`
2. Add Dockerfile with appropriate FROM statement
3. Update `ALL_IMAGES` in Makefile (in dependency order)
4. Update package hierarchy in `.github/workflows/docker.yml`:
   - Add build jobs for each architecture (e.g., `x86_64-<image-name>`, `aarch64-<image-name>`)
   - Add to tag-push matrix or include section
   - Add to needs list in tag-push job
5. **Update `.mergify.yml`** to include CI checks for the new image:
   - Add build-test-upload checks for each architecture
   - Add tag-push checks for each variant
   - Format: `check-success = <platform>-<image> / build-test-upload`
   - Format: `check-success=tag-push (<image-name>, <variant>) / tag-push`
6. Update test dependencies in `tests/hierarchy/`
7. Add tests in `/tests/by_image/<new-image-name>/`
8. Update documentation

### Adding an Image Variant (e.g., CUDA)

When adding a variant to an existing image (like `singlecell-notebook:cuda12`):

1. Create variant subdirectory in `/images/<image-name>/<variant>/`
2. Add variant Dockerfile with appropriate FROM statement
3. Update `.github/workflows/docker.yml`:
   - Add build job for the variant (e.g., `x86_64-<image>-<variant>`)
   - Add to tag-push matrix include section
   - Add to needs list in tag-push job
4. **Update `.mergify.yml`** to include CI checks:
   - Add build-test-upload check: `check-success = x86_64-<image>-<variant> / build-test-upload`
   - Add tag-push check: `check-success=tag-push (<image-name>, <variant>) / tag-push`
5. Add tests in `/tests/by_image/<image-name>/<variant>/`
6. Update documentation

### Updating Dependencies

1. **Prefer mamba for package installation** (check availability for both x86_64 and aarch64)
2. If not available via mamba for both architectures, use pip (Python) or R install methods
3. Modify Dockerfile with new package requirements
4. If package name differs from import name, update `PACKAGE_MAPPING` in `tests/by_image/docker-stacks-foundation/test_packages.py`
5. Rebuild image to test
6. Run tests to ensure nothing breaks
7. Update manifest documentation

### Fixing CI/CD Issues

1. Check GitHub Actions logs in `.github/workflows/`
2. Review test failures in pytest output
3. Verify Docker build steps
4. **Ensure all pre-commit hooks pass** - common issues:
   - **flake8**: Check for code quality issues (unused imports, line length, etc.)
   - **isort**: Ensure imports are sorted correctly (no blank lines between third-party imports)
   - **markdownlint**: Check line length (max 200 chars) and formatting
   - Run locally: `pre-commit run --all-files` to catch issues before pushing

## Security Considerations

- Keep base images up to date (Ubuntu 24.04 currently)
- Regularly update Python and R packages
- Follow security best practices in Dockerfiles
- Review Dependabot PRs promptly

## External Resources

- Main documentation: <https://sequencing-docker-stacks.readthedocs.io/>
- Docker registry: <https://quay.io/organization/huchlab>
- Jupyter Docker Stacks guide: <https://github.com/jupyter/docker-stacks>
