# Copilot Instructions for Sequencing Docker Stacks

## Repository Overview

This repository provides **Sequencing Docker Stacks** - ready-to-run Docker images tailored for sequencing data analysis. The images are based on the [jupyter/docker-stacks](https://github.com/jupyter/docker-stacks) and built upon the Singularity Single Cell container.

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

## Development Guidelines

### Code Style

- Follow existing code conventions
- Use pre-commit hooks (configured in `.pre-commit-config.yaml`)
- Python code should follow PEP 8 (enforced by flake8)
- Dockerfiles should follow best practices (checked by hadolint)
- Markdown should follow markdownlint rules

### Docker Images

- All images inherit from a base image in dependency order
- Use BuildKit for builds (`DOCKER_BUILDKIT=1`)
- Images support both x86_64 and aarch64 architectures
- Tag structure: `quay.io/huchlab/<image-name>:<tag>`

### Testing

- Run tests with `make test/<image-name>` or `python3 -m tests.run_tests`
- Tests are organized by image in `tests/by_image/`
- Shared tests are in `tests/shared_checks/`
- All tests use pytest framework

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
- `.flake8`: Python linting configuration
- `.hadolint.yaml`: Dockerfile linting configuration
- `.markdownlint.yaml`: Markdown linting configuration

## Common Tasks

### Adding a New Image

1. Create directory in `/images/<new-image-name>/`
2. Add Dockerfile with appropriate FROM statement
3. Update `ALL_IMAGES` in Makefile
4. Add tests in `/tests/by_image/<new-image-name>/`
5. Update documentation

### Updating Dependencies

1. Modify Dockerfile or conda/pip requirements
2. Rebuild image to test
3. Run tests to ensure nothing breaks
4. Update manifest documentation

### Fixing CI/CD Issues

1. Check GitHub Actions logs in `.github/workflows/`
2. Review test failures in pytest output
3. Verify Docker build steps
4. Ensure all pre-commit hooks pass

## Security Considerations

- Keep base images up to date (Ubuntu 24.04 currently)
- Regularly update Python and R packages
- Follow security best practices in Dockerfiles
- Review Dependabot PRs promptly

## External Resources

- Main documentation: https://sequencing-docker-stacks.readthedocs.io/
- Docker registry: https://quay.io/organization/huchlab
- Jupyter Docker Stacks guide: https://github.com/jupyter/docker-stacks
