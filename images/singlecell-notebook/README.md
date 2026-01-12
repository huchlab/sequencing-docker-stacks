# Jupyter Notebook Singlecell Stack

GitHub Actions in the <https://github.com/huchlab/sequencing-docker-stacks> project builds and pushes this image to the Registry.

Please visit the [project site](https://github.com/huchlab/sequencing-docker-stacks) for help to use and contribute to this image and others.

## Notes

- **HSMMSingleCell dependency**: The `bioconductor-hsmmsinglecell` package is explicitly installed because it is required by `monocle` at load time.
  Without it, loading `monocle` in R fails with "there is no package called 'HSMMSingleCell'".
