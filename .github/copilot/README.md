# GitHub Copilot Agent Configuration

This directory contains configuration files for GitHub Copilot to provide better assistance when working on the Sequencing Docker Stacks repository.

## Files

### instructions.md

This file provides comprehensive instructions and context about the repository structure, development guidelines, and common tasks. It helps Copilot understand:

- Repository overview and purpose
- Available container images
- Key technologies used
- Development workflow
- Testing and building processes
- Documentation practices

### knowledge.md

This file contains detailed technical knowledge about:

- Image hierarchy and dependencies
- Python and R environments
- Docker build process
- Testing strategies
- CI/CD pipelines
- Common debugging tips
- Architecture support

### copilot-config.yml

Configuration file that specifies:

- Primary languages and frameworks
- Code style preferences
- Testing framework details
- Documentation tools
- Build system information
- Repository conventions

## Purpose

These configuration files enable GitHub Copilot to:

1. **Understand Context**: Copilot can better understand the project structure, dependencies, and workflows
2. **Provide Better Suggestions**: Code suggestions are more relevant to the project's technologies and patterns
3. **Follow Conventions**: Suggestions align with the repository's coding standards and best practices
4. **Assist with Tasks**: Help with common development tasks like building images, running tests, and updating documentation

## How It Works

When GitHub Copilot is active in this repository, it automatically reads these configuration files to understand the project context. This allows it to:

- Suggest code that follows the project's style guidelines
- Recommend appropriate testing approaches
- Help with Docker-specific tasks
- Understand the bioinformatics domain context
- Provide relevant examples from the codebase

## Maintaining These Files

These configuration files should be updated when:

- New images or major features are added
- Development workflows change
- New technologies or tools are adopted
- Testing strategies evolve
- Documentation practices are updated

## Permissions

The configuration files in this directory are accessible to:

- Repository maintainers
- Contributors with write access
- GitHub Copilot service (read-only)

No sensitive information should be stored in these files.

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Repository README](../../README.md)
- [Contributing Guidelines](../../CONTRIBUTING.md)
- [Project Documentation](https://sequencing-docker-stacks.readthedocs.io/)
