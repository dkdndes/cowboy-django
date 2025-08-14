# Release & Publish — Versioning, Releases, and Docker Images

This project uses Conventional Commits + semantic-release to auto-bump versions and publish Docker images to GitHub Container Registry (GHCR). It supports:

- Pure numeric SemVer (no -beta/-rc)
- develop → version bump + Docker :vX.Y.Z and :develop (no GitHub Release)
- main → version bump + GitHub Release + Docker :vX.Y.Z and :latest
- Local dry-run testing with act (no publishing)

## Repo Files & Layout

```
.github/
  workflows/
    release.yml                 # Production workflow (develop/main)
    release-act-test.yml        # Local/feature dry-run tester

.releaserc.main.json            # semantic-release config f
for main

.releaserc.develop.json         # semantic-release config 
for develop

package.json                    # JS tooling manifest for 
semantic-release

docs/
  release-and-publish.md        # ← this file
```

Do not commit **node_modules/.** Add it to **.gitignore.**

## Commit Conventions (drive version bumps)

Use Conventional Commits in PR titles/merge commits:
- feat(scope): … → minor
- fix(scope): … → patch
- docs|ci|test|refactor(scope): … → patch (configured)
- BREAKING CHANGE: … (in body) → major

**Examples:**

- **feat(api)**: add cowboy joke endpoint
- **fix(ui)**: prevent double fetch on refresh
- **docs(readme)**: add local dev instructions

You can tighten rules (e.g., make docs no-release) by adjusting .releaserc.*.json.

## What Each Workflow Does

### 1) Production workflow — .github/workflows/release.yml

**Triggers**: pushes to develop and main

**Does:**
- Runs semantic-release with the right config
- Builds Docker images with OCI labels
- Pushes images to GHCR (unless you set DRY_RUN=true)
- develop: tags vX.Y.Z and develop (no GitHub Release)
- main: tags vX.Y.Z and latest, creates GitHub Release

**Requires permissions:**
permissions: { contents: write, packages: write } (already in the workflow)

**Environment variable:**

- DRY_RUN — if set to "true", skips publishing (useful for tests)

### 2) Local test workflow — .github/workflows/release-act-test.yml

**Triggers:** pushes to feature/** and manual workflow_dispatch

**Does:**
- Always dry-run semantic-release using the develop config
- Builds the Docker image locally (no push) and tags :vX.Y.Z + :develop
- Prints docker images for sanity

**Purpose:** validate everything with act or in feature branches without publishing.

## How to Test Locally with act

**Prerequisites**
- Docker Desktop installed
- act installed

**macOS:**
```
brew install act
```

Recommended runner image pulled (manually) once:

```
docker pull catthehacker/ubuntu:act-latest
```

### 1) Dry-run the test workflow on a feature branch

From repo root:

```
act push \
    -W .github/workflows/release-act-test.yml \
    -j build-release-dry-run \
    -P ubuntu-latest=catthehacker/ubuntu:act-latest \
    --container-architecture linux/amd64 \
    --pull=false \
    -e <(printf '{"ref":"refs/heads/feature/test-ci"}')
```

You’ll see:
- semantic-release dry-run message (no publish on feature/*)
- Docker build completes
- Local images ghcr.io/<owner>/<repo>:vX.Y.Z and :develop appear

### 2) Dry-run on develop (local)

```
act push \
    -W .github/workflows/release-act-test.yml \
    -j build-release-dry-run \
    -P ubuntu-latest=catthehacker/ubuntu:act-latest \
    --container-architecture linux/amd64 \
    --pull=false \
    -e <(printf '{"ref":"refs/heads/develop"}')
```

### 3) (Optional) Real publish from act

Only if you truly want to publish from your machine:
- Provide a PAT with contents:write and packages:write
- Use the production workflow release.yml
- Disable dry-run

```
ACT_DRY=false

act push \
    -W .github/workflows/release.yml \
    -j build-release-publish \
    -P ubuntu-latest=catthehacker/ubuntu:act-latest \
    --container-architecture linux/amd64 \
    --pull=false \
    -s GITHUB_TOKEN=<YOUR_PAT_WITH_CONTENTS_AND_PACKAGES> \
    -s GH_TOKEN=<YOUR_PAT_WITH_CONTENTS_AND_PACKAGES> \
    -s DRY_RUN=$ACT_DRY \
    -e <(printf '{"ref":"refs/heads/develop"}')
```

For normal usage, you don’t need to publish from act. Push to GitHub and let Actions handle it.


## How Versions Are Determined

semantic-release analyzes commits since the last tag:

- feat: → bump minor → 1.3.0
- fix: / docs: / ci: / test: / refactor: → bump patch → 1.2.4
- BREAKING CHANGE: → bump major → 2.0.0

On develop:

- Version increments, CHANGELOG.md updates, commit back to branch
- Docker pushed to GHCR as :vX.Y.Z and :develop (when not dry-run)
- No GitHub Release created

On main:

- Same versioning steps
- GitHub Release is created (with notes)
- Docker pushed as :vX.Y.Z and :latest


## Docker Images & Repo Association

Images are built with OCI labels so GitHub links them to your repo automatically:

- org.opencontainers.image.source=https://github.com/<owner>/<repo>
- org.opencontainers.image.revision=<git-sha>
- org.opencontainers.image.version=v<version>

Tags used:
- develop → :vX.Y.Z and :develop
- main → :vX.Y.Z and :latest

Package appears under Repo → Packages once first push succeeds (and visibility is set appropriately).


## Minimal Commands Cheat-Sheet

### Pull latest stable:

```
docker pull ghcr.io/<owner>/<repo>:latest
```

### Pull specific version:

```
docker pull ghcr.io/<owner>/<repo>:v1.2.3
```

### Pull develop channel:

```
docker pull ghcr.io/<owner>/<repo>:develop
```

## Troubleshooting

- Workflow doesn’t run on branch X
Ensure the workflow file exists in that branch and on: matches the branch name.
- No version bump?
Check that your merge commit/PR title uses Conventional Commit format.
- Package not visible in repo Packages
First successful GHCR push + OCI labels are required. Then set Package visibility Public if needed.
- act hangs on npm install
Add network diagnostics and increase npm timeouts; see our release-act-test.yml (has resilient settings). Use --pull=false if you already have the runner image.

## Maintenance Notes

- Keep semantic-release plugins pinned (you can loosen later).
- Protect main and require PRs.
- (Optional) Add commit linting to enforce Conventional Commits in PRs.