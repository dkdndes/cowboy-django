# Release & Publish Documentation

This document has been updated to reflect the current Python-based release automation system.

## Overview

This project uses Python semantic-release with automated Docker publishing for Django projects. The system has been migrated from Node.js to Python tooling for better Django integration.

## Current Workflow Documentation

For detailed information about the current release and Docker workflows, please see:

### 📋 Workflow Documentation
- **[Python Semantic Release Workflow](python-semantic-release-workflow.md)** - Automated versioning and GitHub releases
- **[Docker Build & Publish Workflow](docker-build-publish-workflow.md)** - Automated Docker image publishing

### 📚 Project Documentation  
- **[Cowboy Django Project](cowboy-django-project.md)** - Complete project documentation and setup

## Migration Summary

The project has been migrated from Node.js semantic-release to Python semantic-release with the following improvements:

### ✅ **What Changed**
- **Node.js → Python**: Now uses `python-semantic-release` instead of Node.js semantic-release
- **Configuration**: Moved from `.releaserc.*.json` files to `pyproject.toml`
- **Workflow Separation**: Split semantic release and Docker publishing into separate workflows
- **Django Integration**: Better integration with Django projects and uv package manager

### ✅ **What Improved**
- **No More Parser Errors**: Eliminated persistent Node.js semantic-release parsing issues
- **Django-Style Versioning**: Pre-releases use Django conventions (e.g., `v2.0.1-a.1`)
- **Better Python Integration**: Native Python tooling for Python projects
- **Separated Concerns**: Independent semantic release and Docker workflows
- **Improved Reliability**: More stable and maintainable automation

### ✅ **Current Release Flow**
1. **Develop Branch** → Creates pre-releases (e.g., `v2.0.1-a.1`)
2. **Main Branch** → Creates stable releases (e.g., `v2.0.1`)
3. **Docker Images** → Automatically built and published for both branches
4. **GitHub Releases** → Automated release notes and changelogs

## Quick Reference

### Available Docker Images
- **Latest stable**: `ghcr.io/dkdndes/cowboy-django:latest`
- **Development**: `ghcr.io/dkdndes/cowboy-django:develop`
- **Specific versions**: `ghcr.io/dkdndes/cowboy-django:v2.0.1`
- **Pre-releases**: `ghcr.io/dkdndes/cowboy-django:v2.0.1-a.1`

### Conventional Commit Examples
```bash
# Minor version bump (feature)
feat(api): add new cowboy joke endpoint

# Patch version bump (fix)
fix(ui): resolve ASCII art display issue

# Major version bump (breaking change)
feat(api): restructure response format

BREAKING CHANGE: API now returns jokes in new JSON structure
```

### Local Testing
```bash
# Test semantic release (dry run)
uv run semantic-release version --dry-run

# Check what version would be released
uv run semantic-release version --print

# Test Docker build
docker build -t test-build .
docker run -p 8000:8000 test-build
```

## Legacy Information

The following components are no longer used but may be referenced in old documentation:

### ❌ **Removed Components**
- `package.json` and `package-lock.json` (Node.js dependencies)
- `.releaserc.develop.json` and `.releaserc.main.json` (old configuration)
- `.github/workflows/release.yml` (monolithic workflow)
- `.github/workflows/release-act-test.yml` (local testing workflow)

### ❌ **Deprecated Commands**
```bash
# These commands no longer work:
npm install
npm run semantic-release
act push -W .github/workflows/release-act-test.yml
```

## For New Django Projects

To implement this release system in your own Django project:

1. **Copy Workflow Files**:
   - `.github/workflows/python-release.yml`
   - `.github/workflows/docker-publish.yml`

2. **Configure in `pyproject.toml`**:
   ```toml
   [tool.semantic_release]
   version_variables = ["pyproject.toml:project.version"]
   # ... see workflow documentation for full configuration
   ```

3. **Add Dependencies**:
   ```toml
   [dependency-groups]
   dev = [
       "python-semantic-release>=9.0.0",
   ]
   ```

4. **Set Repository Permissions**:
   - Settings → Actions → General → "Read and write permissions"

See the individual workflow documentation files for complete setup instructions and examples.

## Support

For questions about the current release system:
1. Check the individual workflow documentation files
2. Review the GitHub Actions logs for specific runs
3. Test locally using the semantic-release commands shown above
4. Open an issue in the repository for bugs or improvements

This migration represents a significant improvement in reliability and maintainability for Django project automation.