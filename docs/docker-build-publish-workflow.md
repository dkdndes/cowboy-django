# Docker Build & Publish Workflow

This document describes the Docker Build & Publish workflow for automatically building and publishing Docker images to GitHub Container Registry (GHCR) based on successful semantic releases.

## Overview

The Docker Build & Publish workflow (`docker-publish.yml`) builds Docker images and publishes them to GHCR whenever a semantic release workflow completes successfully. It creates different tags for different branches and ensures images are properly labeled for GitHub integration.

## Workflow File Location

```
.github/workflows/docker-publish.yml
```

## When It Runs

**Trigger:**
- `workflow_run` - Automatically triggered when "Python Semantic Release" workflow completes successfully
- Runs for both `develop` and `main` branches
- Only runs if the semantic release workflow was successful

## What It Does

### For All Successful Runs
1. **Checks out code** from the branch that triggered the semantic release
2. **Retrieves version information** from the latest GitHub release
3. **Logs into GitHub Container Registry** using repository token
4. **Builds Docker image** with proper OCI labels
5. **Tags image** with version and branch-specific tags
6. **Pushes images** to GHCR
7. **Provides summary** of published images

### Branch-Specific Behavior

#### Develop Branch
- **Version tag**: `v2.0.1-a.1` (from pre-release)
- **Numeric tag**: `2.0.1-a.1` (without 'v' prefix)
- **Branch tag**: `develop` (latest develop build)

#### Main Branch
- **Version tag**: `v2.0.1` (from stable release)
- **Numeric tag**: `2.0.1` (without 'v' prefix)  
- **Latest tag**: `latest` (latest stable release)

## Configuration

### Registry Settings

```yaml
env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}
  DOCKER_BUILDKIT: "1"
```

### Required Permissions

```yaml
permissions:
  contents: write        # To read repository and releases
  packages: write        # To push to GitHub Container Registry
  security-events: write # For security scanning integration
```

## Docker Image Labels

All images are built with comprehensive OCI labels for GitHub integration:

```dockerfile
--label org.opencontainers.image.source=https://github.com/${{ github.repository }}
--label org.opencontainers.image.revision=${{ github.event.workflow_run.head_sha }}
--label org.opencontainers.image.version=$TAG
--label org.opencontainers.image.created=$(date -u +'%Y-%m-%dT%H:%M:%SZ')
--label org.opencontainers.image.title="Cowboy Django"
--label org.opencontainers.image.description="Django + HTMX web app with ASCII art cowboys and Kubernetes jokes"
```

These labels ensure:
- **Automatic linking** to your GitHub repository
- **Proper versioning** information
- **Build traceability** with Git SHA
- **Metadata** for package discovery

## Image Tagging Strategy

### Develop Branch Releases
For pre-release `v2.0.1-a.1`:
```bash
ghcr.io/owner/repo:v2.0.1-a.1    # Full version tag
ghcr.io/owner/repo:2.0.1-a.1     # Numeric version
ghcr.io/owner/repo:develop        # Latest develop
```

### Main Branch Releases  
For stable release `v2.0.1`:
```bash
ghcr.io/owner/repo:v2.0.1         # Full version tag
ghcr.io/owner/repo:2.0.1          # Numeric version
ghcr.io/owner/repo:latest         # Latest stable
```

## Integration with Django Projects

### Dockerfile Requirements

Your Django project needs a `Dockerfile` in the repository root. Example structure:

```dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run Django application
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Project Structure Requirements
```
your-django-project/
├── Dockerfile                     # Docker build instructions
├── .dockerignore                  # Files to exclude from build
├── pyproject.toml                 # Python project configuration
├── uv.lock                        # Dependency lock file
├── .github/workflows/
│   ├── python-release.yml         # Triggers this workflow
│   └── docker-publish.yml         # This workflow
└── your Django app files
```

## Usage Examples

### Setting Up in a New Django Project

1. **Copy the workflow file:**
```bash
mkdir -p .github/workflows
cp docker-publish.yml .github/workflows/
```

2. **Create or update .dockerignore:**
```
.git
.github
__pycache__/
*.pyc
.pytest_cache/
.coverage
htmlcov/
.env
.env.*
docs/
*.md
tests/
```

3. **Ensure proper GitHub permissions:**
   - Go to repository Settings → Actions → General
   - Set "Workflow permissions" to "Read and write permissions"
   - Enable "Allow GitHub Actions to create and approve pull requests"

### Customizing for Your Project

#### Update Image Labels
Modify the build step in the workflow:

```yaml
--label org.opencontainers.image.title="Your Django Project"
--label org.opencontainers.image.description="Your project description"
```

#### Change Registry or Image Name
Update the environment variables:

```yaml
env:
  REGISTRY: your-registry.io        # Change registry
  IMAGE_NAME: custom/image-name     # Change image name
```

#### Add Multi-Platform Builds
Extend the workflow to build for multiple architectures:

```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3

- name: Build Docker image with labels
  run: |
    docker buildx build \
      --platform linux/amd64,linux/arm64 \
      --push \
      # ... existing labels and tags
```

## Local Testing

### Test Docker Build Locally

```bash
# Build image locally with same tags
docker build \
  --label org.opencontainers.image.source=https://github.com/owner/repo \
  --label org.opencontainers.image.version=v1.0.0 \
  -t ghcr.io/owner/repo:v1.0.0 \
  -t ghcr.io/owner/repo:latest \
  .

# Run locally to test
docker run -p 8000:8000 ghcr.io/owner/repo:latest
```

### Test with Different Python Versions

```bash
# Build with specific Python version
docker build --build-arg PYTHON_VERSION=3.11 -t test-image .
```

## Pulling and Using Images

### Pull Latest Stable Release
```bash
docker pull ghcr.io/owner/repo:latest
docker run -p 8000:8000 ghcr.io/owner/repo:latest
```

### Pull Specific Version
```bash
docker pull ghcr.io/owner/repo:v2.0.1
docker run -p 8000:8000 ghcr.io/owner/repo:v2.0.1
```

### Pull Development Version
```bash
docker pull ghcr.io/owner/repo:develop
docker run -p 8000:8000 ghcr.io/owner/repo:develop
```

### Pull Pre-release Version
```bash
docker pull ghcr.io/owner/repo:v2.0.1-a.1
docker run -p 8000:8000 ghcr.io/owner/repo:v2.0.1-a.1
```

## Monitoring and Debugging

### View Published Packages
1. Go to your repository on GitHub
2. Click "Packages" tab (or check your profile packages)
3. Find your container package
4. View all published tags and their details

### Check Workflow Logs
1. Repository → Actions → "Docker Build & Publish"
2. Click on specific workflow run
3. Expand each step to see detailed logs
4. Look for build errors or push failures

### Common Workflow Outputs

**Successful run summary:**
```
## Docker Build & Publish Summary
- **Version**: 2.0.1
- **Tag**: v2.0.1  
- **Branch**: main
- **Images pushed**:
  - ghcr.io/owner/repo:v2.0.1
  - ghcr.io/owner/repo:2.0.1
  - ghcr.io/owner/repo:latest
```

## Troubleshooting

### Common Issues

**Permission denied when pushing:**
- Verify repository has "Read and write permissions" in Actions settings
- Check that `GITHUB_TOKEN` has packages:write permission
- Ensure package doesn't have conflicting permissions

**Workflow doesn't trigger:**
- Verify "Python Semantic Release" workflow completed successfully
- Check that workflow_run trigger configuration matches workflow name exactly
- Ensure both workflows exist on the same branch

**Docker build fails:**
- Check Dockerfile syntax and requirements
- Verify all COPY sources exist in repository
- Check .dockerignore isn't excluding required files

**Images not visible in GitHub:**
- First push must succeed with proper OCI labels
- Package visibility might need to be set to "Public"
- Check that image was actually pushed (not just built)

### Debug Steps

1. **Check semantic release outputs:**
```bash
# In the workflow run logs, verify:
# - released=true
# - version=X.Y.Z  
# - tag=vX.Y.Z
```

2. **Test Docker build locally:**
```bash
# Clone repo and build manually
git clone https://github.com/owner/repo
cd repo
docker build -t test-build .
```

3. **Verify GHCR authentication:**
```bash
# Test login locally
echo $GITHUB_TOKEN | docker login ghcr.io -u owner --password-stdin
```

## Security Considerations

### Token Permissions
- Workflow uses `GITHUB_TOKEN` with minimal required permissions
- Tokens are automatically scoped to the repository
- No need to create personal access tokens

### Image Security
- Images include Git SHA for build traceability
- All builds are reproducible from Git commits
- Consider adding security scanning to workflow

### Package Visibility
- Packages default to repository visibility settings
- Consider making stable releases public
- Keep development images private if needed

## Advanced Configuration

### Adding Build Arguments
```yaml
- name: Build Docker image with labels
  run: |
    docker build \
      --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
      --build-arg VERSION=$VERSION \
      # ... rest of build command
```

### Multi-Stage Builds
Optimize for Django applications:
```dockerfile
# Build stage
FROM python:3.12-slim as builder
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen

# Runtime stage  
FROM python:3.12-slim
COPY --from=builder /app/.venv /app/.venv
COPY . /app
WORKDIR /app
CMD ["/app/.venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
```

This workflow ensures that every successful release automatically gets a corresponding Docker image, making deployment and distribution seamless for Django projects.