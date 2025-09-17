# Docker stacks testing

Please, refer to the [testing section of documentation](https://jupyter-docker-stacks.readthedocs.io/en/latest/contributing/tests.html) to see how the tests are run.

## Running specific tests

From root of the repository, run

```bash
export TEST_IMAGE=quay.io/huchlab/singlecell-notebook
python3 -m pytest --numprocesses auto -m "not info" \
    -k "test_reticulate" \
    ./tests/by_image/singlecell-notebook/
```
