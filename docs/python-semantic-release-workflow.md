# Python Semantic Release Workflow

This document describes the Python Semantic Release workflow for automatic versioning and release management in Django projects.

## Overview

The Python Semantic Release workflow (`python-release.yml`) provides automated versioning and GitHub release creation based on conventional commit messages. It uses `python-semantic-release` which is specifically designed for Python projects and integrates well with Django applications.

## Workflow File Location

```
.github/workflows/python-release.yml
```

## When It Runs

**Triggers:**
- Push to `develop` branch → Creates pre-releases (e.g., `v2.0.1-a.1`)
- Push to `main` branch → Creates stable releases (e.g., `v2.0.1`)

## What It Does

### For Develop Branch
1. **Analyzes commits** since last release using conventional commit format
2. **Creates pre-release versions** with Django-style alpha suffix (e.g., `v2.1.0-a.3`)
3. **Creates Git tag** for the version (no file commits)
4. **Updates CHANGELOG.md** with new changes
5. **Creates GitHub pre-release** (marked as pre-release)
6. **Outputs version info** for downstream workflows (Docker build)

### For Main Branch
1. **Analyzes commits** since last release
2. **Creates stable release versions** (e.g., `v2.1.1`)
3. **Creates Git tag** for the version (no file commits)
4. **Updates CHANGELOG.md** with finalized changes
5. **Creates GitHub release** (stable, not pre-release)
6. **Outputs version info** for downstream workflows

### Git Tag-Based Versioning
This workflow uses **Git tags only** for version management:
- ✅ **No version files** to maintain in the codebase
- ✅ **No version bump commits** that create merge conflicts
- ✅ **Pure Git tag discovery** via setuptools_scm
- ✅ **Clean branch synchronization** between develop and main

## Configuration

### Branch Configuration

The workflow behavior is configured in `pyproject.toml`:

```toml
[tool.semantic_release.branches.main]
match = "main"
prerelease = false

[tool.semantic_release.branches.develop]
match = "develop"
prerelease = true
prerelease_token = "a"
```

### Version Management

```toml
[tool.semantic_release]
version_variables = ["pyproject.toml:project.version"]
build_command = """
    python -m pip install -e '.[build]'
    uv lock --upgrade-package django-cowboy-htmx-rotator
    git add uv.lock
"""
major_on_zero = false
tag_format = "v{version}"
```

### Commit Message Rules

```toml
[tool.semantic_release.commit_parser_options]
allowed_tags = ["build", "chore", "ci", "docs", "feat", "fix", "perf", "style", "refactor", "test"]
minor_tags = ["feat"]
patch_tags = ["fix", "perf", "refactor", "build", "chore", "ci", "docs", "style", "test"]
```

## Conventional Commit Format

Use these commit message patterns to trigger version bumps:

### Minor Version Bump (1.2.0 → 1.3.0)
```bash
feat(scope): add new feature description

# Examples:
feat(api): add cowboy joke endpoint
feat(ui): implement ASCII art rotation
```

### Patch Version Bump (1.2.0 → 1.2.1)
```bash
fix(scope): fix bug description
refactor(scope): improve code structure
docs(scope): update documentation
chore(scope): update dependencies

# Examples:
fix(models): resolve cowboy joke duplication
docs(readme): add installation instructions
chore(deps): update Django to 5.0.1
```

### Major Version Bump (1.2.0 → 2.0.0)
```bash
feat(scope): add breaking change

BREAKING CHANGE: This change removes the old API endpoint and replaces it with a new one.

# Example:
feat(api): restructure joke response format

BREAKING CHANGE: The API now returns jokes in a different JSON structure.
```

## Required Permissions

The workflow requires these GitHub permissions:

```yaml
permissions:
  contents: write        # To push version commits and create releases
  pull-requests: write   # To create pull requests if needed
```

## Environment Setup

### Python Dependencies
The workflow automatically installs:
- Python 3.12
- uv package manager
- python-semantic-release

### Git Configuration
The workflow configures Git with:
- User: `semantic-release`
- Email: `semantic-release@users.noreply.github.com`

## Integration with Django Projects

### Project Structure Requirements
```
your-django-project/
├── pyproject.toml              # Must contain [tool.semantic_release] config
├── .github/workflows/
│   └── python-release.yml     # This workflow
├── requirements files or uv setup
└── your Django app files
```

### Django-Specific Benefits
1. **Python-native tooling** - Uses Python semantic-release instead of Node.js
2. **uv integration** - Automatically updates `uv.lock` with new versions
3. **Django versioning** - Follows Django's alpha/beta/rc conventions
4. **Git tag-based versioning** - No version files, pure Git tag discovery
5. **Clean workflows** - No version bump commits prevent merge conflicts

## Usage Examples

### Setting Up in a New Django Project

1. **Copy the workflow file:**
```bash
mkdir -p .github/workflows
cp python-release.yml .github/workflows/
```

2. **Configure dynamic versioning in `pyproject.toml`:**
```toml
[project]
name = "your-project-name"
dynamic = ["version"]  # Use Git tags for version discovery
description = "Your project description"
# ... other project metadata

[build-system]
requires = ["setuptools>=61", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
packages = ["your_main_package", "your_django_apps"]

[tool.setuptools_scm]
# Git tag-based version discovery (no files written)

[tool.semantic_release]
build_command = """
    uv sync --dev
    uv lock --upgrade-package your-project-name
"""
commit = false  # No version bump commits
major_on_zero = false
tag_format = "v{version}"

[tool.semantic_release.branches.main]
match = "main"
prerelease = false

[tool.semantic_release.branches.develop]
match = "develop" 
prerelease = true
prerelease_token = "a"

[tool.semantic_release.commit_parser_options]
allowed_tags = ["build", "chore", "ci", "docs", "feat", "fix", "perf", "style", "refactor", "test"]
minor_tags = ["feat"]
patch_tags = ["fix", "perf", "refactor", "build", "chore", "ci", "docs", "style", "test"]
```

3. **Add python-semantic-release to dependencies:**
```toml
[dependency-groups]
dev = [
    "python-semantic-release>=9.0.0",
    # ... other dev dependencies
]
```

### Local Testing

Test semantic release locally without creating actual releases:

```bash
# Install dependencies
uv sync --dev

# Dry run to see what version would be created
uv run semantic-release version --dry-run

# Check what version would be released
uv run semantic-release version --print

# Generate changelog without releasing
uv run semantic-release changelog
```

## Troubleshooting

### Common Issues

**No version bump created:**
- Check that commit messages follow conventional format
- Ensure commits exist since last release
- Verify branch configuration matches actual branch names

**Permission denied errors:**
- Ensure repository has "Read and write permissions" in Settings → Actions → General
- Check that `GITHUB_TOKEN` has sufficient permissions

**Build command fails:**
- Verify `uv.lock` file exists and is valid
- Check that project name in build command matches actual project
- Ensure all build dependencies are available

**Wrong version format:**
- Check `tag_format` setting in `pyproject.toml`
- Verify `prerelease_token` is set correctly for develop branch

### Debugging Workflow

View workflow logs in GitHub Actions:
1. Go to your repository → Actions tab
2. Click on "Python Semantic Release" workflow
3. Click on specific run to see detailed logs
4. Check each step for error messages

## Version Flow Example

### Development Cycle
```
1. Work on develop branch
   └─ feat: add new feature
   └─ Triggers: v2.0.1-a.1 (pre-release)

2. More work on develop
   └─ fix: bug fix
   └─ Triggers: v2.0.1-a.2 (pre-release)

3. Merge develop to main
   └─ Triggers: v2.0.1 (stable release)
```

### Release Timeline
- **develop**: `v2.0.1-a.1` → `v2.0.1-a.2` → `v2.0.1-a.3` (pre-releases)
- **main**: `v2.0.1` (stable release when merged from develop)

This ensures that:
- Development iterations are tracked with pre-releases
- Main branch only contains stable, tested releases
- Version history is clear and follows Django conventions