# Docker Image Streaming Optimizations

## Summary

This repository's GitHub Actions workflows have been optimized to make extensive use of Docker's ability to stream images directly to container registries during build, significantly reducing local disk space usage.

## Key Optimizations Implemented

### 1. Direct Streaming During Build (docker-build-upload.yml)

**Location:** `.github/workflows/docker-build-upload.yml` (lines 111-130)

The workflow uses `docker buildx build --push` to build and stream images directly to GitHub Container Registry (GHCR) without storing them locally first:

```yaml
docker buildx build \
  --rm --force-rm \
  --tag ghcr.io/$OWNER/sequencing-docker-stacks/$IMAGE:build-$SHA-$RUN_ID-$PLATFORM-$VARIANT \
  --push \
  images/$IMAGE/$VARIANT/
```

**Benefits:**
- Images are streamed layer-by-layer to GHCR as they're built
- No intermediate storage of the full image on the runner's disk
- Saves 1-10+ GB per image depending on size
- Build artifacts are immediately available to downstream jobs

### 2. Registry-to-Registry Image Copying (copy-and-tag-image action)

**Location:** `.github/actions/copy-and-tag-image/action.yml` and `tagging/apps/copy_and_tag_image.py`

The workflow uses `docker buildx imagetools create` to copy images directly from GHCR to Quay.io without pulling them to local disk:

```python
docker buildx imagetools create \
  --tag quay.io/$OWNER/$IMAGE:$TAG \
  ghcr.io/$OWNER/sequencing-docker-stacks/$IMAGE:build-$SHA-$RUN_ID-$PLATFORM-$VARIANT
```

**Benefits:**
- No local disk space used for the final tagged images
- Images are copied directly between registries at the network level
- Saves 1-10+ GB per image per platform (typically 2 platforms = 2-20+ GB saved)
- Faster than pull-tag-push workflows

### 3. Direct GHCR Access for Apptainer Builds (apptainer-push.yml)

**Location:** `.github/workflows/apptainer-push.yml` (lines 84-103)

Apptainer builds SIF images directly from GHCR without requiring a local Docker image:

```bash
# Definition file references GHCR image
GHCR_IMAGE="ghcr.io/$OWNER/sequencing-docker-stacks/$IMAGE:build-$SHA-$RUN_ID-x86_64-$VARIANT"
apptainer build /tmp/apptainer/$IMAGE.sif /tmp/apptainer/apptainer.def
```

**Benefits:**
- Apptainer pulls layers directly from GHCR as needed
- No Docker image stored locally during conversion
- Saves additional 1-10+ GB per image

### 4. Temporary Image Storage with Automatic Cleanup

**Location:** `.github/workflows/ghcr-cleanup.yml`

Intermediate build images tagged as `build-{sha}-{run_id}-{platform}-{variant}` are automatically cleaned up from GHCR after 3 days, preventing registry bloat.

## Minimal Necessary Local Storage

The only Docker images stored locally on runners are:

1. **Parent images** (when required): Pulled from GHCR by the `load-image` action only when building child images
2. **One copy for tagging/manifest generation**: After building and pushing, one copy is pulled back temporarily to run containerized inspection scripts that extract metadata for tags and manifests

This minimal approach is necessary because:
- Parent images are needed as base layers for child image builds
- The Python tagging scripts (`write_tags_file.py`, `write_manifest.py`) need to run commands inside containers to extract version information and package lists

## Disk Space Savings

For a typical workflow building ~10 images across 2 platforms:

- **Before optimization:** 20-200+ GB of local disk usage (all images stored locally)
- **After optimization:** ~5-20 GB of local disk usage (only parent images + temporary copies)
- **Savings:** 15-180+ GB per workflow run

## Architecture Flow

```
Build Phase:
  [Build Image] --stream--> [GHCR] 
       |
       v
  [Pull for tagging]
       |
       v
  [Generate tags/manifests]
       |
       v
  [Cleanup local image]

Tag & Push Phase:
  [GHCR Image] --direct copy--> [Quay.io with tags]
  (no local storage)

Apptainer Phase:
  [GHCR Image] --stream--> [Apptainer SIF] --push--> [Quay.io]
  (no Docker storage)
```

## Implementation Notes

1. **GHCR as Intermediate Storage:** GHCR is used as a temporary artifact store instead of GitHub Actions artifacts (which would require saving/loading tar files)

2. **Unique Tagging Scheme:** Images are tagged with commit SHA and run ID to ensure uniqueness across concurrent workflow runs:
   ```
   build-{short-sha}-{run-id}-{platform}-{variant}
   ```

3. **No Force Push:** The workflow avoids any operations that would require force pushing, making it safe for concurrent runs

4. **Minimal Local Operations:** Local image operations are limited to:
   - Running tagging scripts that need container inspection
   - Building child images that need parent images as base layers

## Related Files

- `.github/workflows/docker-build-upload.yml` - Main build workflow with streaming
- `.github/workflows/docker-tag-push.yml` - Tag and push workflow with direct copying
- `.github/actions/load-image/action.yml` - Loads parent images from GHCR when needed
- `.github/actions/copy-and-tag-image/action.yml` - Copies images between registries without local storage
- `.github/workflows/apptainer-push.yml` - Apptainer conversion without local Docker storage
- `.github/workflows/ghcr-cleanup.yml` - Automatic cleanup of temporary GHCR images
- `tagging/apps/copy_and_tag_image.py` - Python script for registry-to-registry copying

## Conclusion

The repository's workflows are already highly optimized for minimal disk space usage. The main techniques employed are:

1. ✅ Stream images to GHCR during build with `--push`
2. ✅ Copy images between registries without local storage
3. ✅ Build Apptainer images directly from remote images
4. ✅ Automatic cleanup of temporary images
5. ✅ Minimal local storage only when absolutely necessary

No further optimizations for Docker image streaming are needed at this time.
