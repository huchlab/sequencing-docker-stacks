import importlib.util

# In default variant, rapids_singlecell is installed, but import would fail because cuml is missing
# In cuda13 variant, cuml is available and rapids_singlecell can be fully imported
if importlib.util.find_spec("cuml") is None:
    # Default variant: just check rapids_singlecell is installed
    assert importlib.util.find_spec("rapids_singlecell") is not None
else:
    # CUDA variant: full import should work
    import rapids_singlecell

    _ = rapids_singlecell.__version__
