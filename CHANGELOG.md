# CHANGELOG


## v1.1.2 (2025-08-16)

### Bug Fixes

- **ci**: Improve Docker image naming and remove unused workflow
  ([`68fd4af`](https://github.com/dkdndes/cowboy-django/commit/68fd4af87b03e2dd29963a9d6dc90b6a7ca51aba))

- Use github.repository_owner for better GHCR compatibility - Remove release-act-test.yml workflow
  (no longer needed) - This should help resolve Docker push permission issues


## v1.1.1 (2025-08-16)

### Bug Fixes

- **ci**: Add id-token permission and debug Docker login
  ([`c7472e2`](https://github.com/dkdndes/cowboy-django/commit/c7472e20b0cd7947308574b205cd72b23779e4de))

- Add id-token: write permission for better GHCR authentication - Add debugging output to Docker
  login step - This should resolve the 'permission_denied: write_package' error


## v1.1.0 (2025-08-16)

### Bug Fixes

- **ci**: Repair semantic-release configuration for any repository
  ([#20](https://github.com/dkdndes/cowboy-django/pull/20),
  [`2569add`](https://github.com/dkdndes/cowboy-django/commit/2569add1a42a8c1ceba6b20e25456a1807df7149))

- Add missing tagFormat to both release configs for consistent v1.2.3 tags - Use GitHub environment
  variables instead of hardcoded repository URLs - Fix semantic-release config path resolution with
  proper ./ prefix - Standardize release rules across develop and main configurations - Add
  comprehensive CLAUDE.md documentation for future development

This makes the release workflow portable to any Django project.

### Chores

- Ignore node_modules
  ([`7464c14`](https://github.com/dkdndes/cowboy-django/commit/7464c14eb95161fb90fb84e5268810c20a3ccb40))

Signed-off-by: PR <dkdndes@gmail.com>

- Ruff fix and ruff format
  ([`dfe8d9b`](https://github.com/dkdndes/cowboy-django/commit/dfe8d9b5b24cc0b568f64fadcb09099fe720df0a))

- Ruff fix and ruff format
  ([`8d4ceae`](https://github.com/dkdndes/cowboy-django/commit/8d4ceae7c49336e3c7f35bcabc4b0b4fa5e4de83))

- **deps**: Add semantic-release toolchain and config to package.json
  ([`cab5ac1`](https://github.com/dkdndes/cowboy-django/commit/cab5ac15317ba0632454d331b2803a1a6baeab45))

- **lockfile**: Update package-lock.json for semantic-release setup
  ([`0f13f56`](https://github.com/dkdndes/cowboy-django/commit/0f13f56d17770d3ab4e07867b6318190b331c12d))

### Documentation

- Ignore nodes_moduls
  ([`2dbd9a4`](https://github.com/dkdndes/cowboy-django/commit/2dbd9a4bd36fff874dc7cf688cb92d3765afd2ea))

- **release**: Add documentation for semantic-release and docker workflows
  ([`778fa8b`](https://github.com/dkdndes/cowboy-django/commit/778fa8b930851068db649c27d6916def4ed1b105))

### Features

- **ci**: Add local dry-run release workflow for act testing
  ([`0a1ca1d`](https://github.com/dkdndes/cowboy-django/commit/0a1ca1d7fdb77cb70a3b74ac52337a36a315b1f7))

- **ci**: Add release workflow for develop and main
  ([`b0fecc5`](https://github.com/dkdndes/cowboy-django/commit/b0fecc5e87641ad798ff3afe39b3e03105463011))

- **release**: Migrate from Node.js to Python semantic-release
  ([#22](https://github.com/dkdndes/cowboy-django/pull/22),
  [`8d41788`](https://github.com/dkdndes/cowboy-django/commit/8d41788313b0896c9bdfd06a6733367adf6de4a8))

* fix(ci): remove problematic parserOpts from semantic-release config

The parserOpts configuration was causing a parsing error in semantic-release. Use default parser
  options which handle BREAKING CHANGE correctly.

* feat(release): migrate from Node.js to Python semantic-release

- Remove all Node.js semantic-release files and dependencies - Add python-semantic-release
  configuration to pyproject.toml - Create new GitHub Actions workflow for Python-based releases -
  Configure uv integration with lock file management - Support both develop and main branch
  workflows - Update CLAUDE.md with new Python-based commands

This replaces the problematic Node.js semantic-release with the Python version that's more
  appropriate for our Django project.


## v1.0.0 (2025-08-14)

### Documentation

- Add comprehensive documentation and MIT license
  ([`b9a4064`](https://github.com/dkdndes/cowboy-django/commit/b9a406415988817bf31a89f7019e41333eff5cb1))

- Complete README with setup instructions - Docker standalone and local development guides -
  Detailed Kubernetes deployment workflow - Project structure and technical highlights - MIT license
  for open source distribution - Future extension roadmap

- Update issue templates
  ([`e9a0df3`](https://github.com/dkdndes/cowboy-django/commit/e9a0df3c449d928b05aeb10ea48f2499bbb09347))

### Features

- Add core Django application with ASCII cowboy jokes
  ([`13d84ef`](https://github.com/dkdndes/cowboy-django/commit/13d84ef3364e3f1498256da573e04f16c1061327))

- Django 5.0+ application with HTMX frontend - ASCII art cowboys with Kubernetes-themed humor -
  JSON-based ASCII art storage (prevents Python syntax issues) - Session-based joke/art rotation
  system - Modern uv dependency management - Dark theme responsive design

- Add Docker containerization with uv
  ([`b09c7c7`](https://github.com/dkdndes/cowboy-django/commit/b09c7c7ea3eb7ab3914d5242e11c1de53988ec0d))

- Multi-stage Docker build optimized for production - Modern uv dependency management integration -
  Proper .dockerignore for optimized build context - ASGI/Uvicorn server configuration - Container
  runs on port 8000

- Add Kubernetes deployment manifests
  ([`f10505b`](https://github.com/dkdndes/cowboy-django/commit/f10505b82c2abea757489cc604f66aca971d29f0))

- Complete K8s manifests with namespace isolation - Init containers for automatic database
  migrations - ClusterIP service configuration - Resource limits and requests - Example nginx
  deployment for testing - Production-ready cowboy namespace setup

- Comprehensive readme
  ([`899cc46`](https://github.com/dkdndes/cowboy-django/commit/899cc4612040d65841e073343128a7c1c6608ab7))
