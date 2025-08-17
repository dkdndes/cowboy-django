# CHANGELOG


## v2.1.0-a.4 (2025-08-17)

### Documentation

- Update README with comprehensive badges and tech stack
  ([`4dc9105`](https://github.com/dkdndes/cowboy-django/commit/4dc910598da1ba3e6bf9090153a49f5e80a7ff5b))

- Add comprehensive badge sections for project status, tech stack, and DevOps tools - Include badges
  for Python, Django, HTMX, uv, Ruff, Semantic Release, Docker, and Kubernetes - Update version
  references to latest v2.1.1 release - Enhance technology stack section with detailed tool
  descriptions - Add GitHub Actions workflow status and Docker image size badges - Improve project
  navigation with organized badge sections


## v2.1.0-a.3 (2025-08-17)

### Documentation

- Remove external tool references from CHANGELOG
  ([`d86f90b`](https://github.com/dkdndes/cowboy-django/commit/d86f90b9dd4955436e038b6763325344d13cdddf))

Clean up changelog entries to remove automated tool attributions while preserving all technical
  content and commit information.


## v2.1.0-a.2 (2025-08-17)

### Bug Fixes

- **ci**: Use stable semantic-release version and Git tag versioning
  ([#28](https://github.com/dkdndes/cowboy-django/pull/28),
  [`3dbcb9f`](https://github.com/dkdndes/cowboy-django/commit/3dbcb9fe6595391ca822336c2744cec58331abc6))

* feat(version): use Git tags for versioning without file commits

- Remove static version from pyproject.toml, use dynamic versioning - Configure setuptools_scm for
  Git tag-based version discovery - Set semantic-release commit=false to avoid version bump commits
  - Add setuptools package discovery for Django app structure - Include both new Kubernetes cowboy
  jokes in views.py

This eliminates the circular reference issue and prevents extra commits on main branch after
  releases, keeping develop and main branches synchronized.

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>

* fix(ci): use stable semantic-release version and Git tag versioning

- Downgrade to python-semantic-release@v9.14.0 for stability - Fix version detection to use Git tags
  instead of pyproject.toml - This aligns with our setuptools_scm Git tag-based approach - Should
  resolve Docker container build issues in the Action

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>

---------

Co-authored-by: Claude <noreply@anthropic.com>


## v2.1.0-a.1 (2025-08-17)

### Bug Fixes

- **project**: Correct project name from django-cowboy-htmx-rotator to cowboy-django
  ([`727fc67`](https://github.com/dkdndes/cowboy-django/commit/727fc677d0afe8db928f081660e6292a330f55e1))

- Update pyproject.toml project name to match repository name - Fix build command package name
  reference - No circular reference issues - version is static string updated by semantic-release

### Features

- **version**: Use Git tags for versioning without file commits
  ([#27](https://github.com/dkdndes/cowboy-django/pull/27),
  [`df8c6ab`](https://github.com/dkdndes/cowboy-django/commit/df8c6ab28e9ba695a91050854e6033f4be51cdac))

- Remove static version from pyproject.toml, use dynamic versioning - Configure setuptools_scm for
  Git tag-based version discovery - Set semantic-release commit=false to avoid version bump commits
  - Add setuptools package discovery for Django app structure - Include both new Kubernetes cowboy
  jokes in views.py

This eliminates the circular reference issue and prevents extra commits on main branch after
  releases, keeping develop and main branches synchronized.

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-authored-by: Claude <noreply@anthropic.com>

- **jokes**: Add two new Kubernetes-themed cowboy jokes
  ([`7e2cfca`](https://github.com/dkdndes/cowboy-django/commit/7e2cfcaba810209001b1b9bf06d7c2a9773f6ae4))

- Add Load Balancer/Ingress joke about denied access - Add volumes mounting joke with cowboy horse
  metaphor - Improves humor variety in the rotation system

- **version**: Implement dynamic versioning without git commits
  ([`575c99e`](https://github.com/dkdndes/cowboy-django/commit/575c99e46ab57240243c89cc437af09042d6d4f3))

- Use setuptools_scm for automatic version from git tags - Remove version_toml to prevent
  semantic-release version commits - Set commit=false to avoid extra commits on main branch - Add
  dynamic version import in cowboysite/__init__.py - Ignore auto-generated _version.py file

This eliminates the merge conflict issue where main gets extra commits after each release, keeping
  develop and main in sync.


## v2.0.3 (2025-08-16)

### Bug Fixes

- **ci**: Resolve version updates and Docker workflow triggers
  ([`105a029`](https://github.com/dkdndes/cowboy-django/commit/105a029d5e32079e2814ee579f7a83a39cb0583c))

- Fix semantic-release configuration: use version_toml instead of version_variables for
  pyproject.toml - Improve Docker workflow trigger reliability with workflow_dispatch fallback - Add
  comprehensive debugging for workflow_run triggers - Support both automatic and manual Docker
  builds


## v2.0.2 (2025-08-16)


## v2.0.2-a.1 (2025-08-16)

### Documentation

- Comprehensive workflow and project documentation
  ([`430a9fa`](https://github.com/dkdndes/cowboy-django/commit/430a9fa8f30c160a1d7b369133a1928ab8a72add))

- Add detailed Python Semantic Release workflow documentation - Add comprehensive Docker Build &
  Publish workflow documentation - Create complete Cowboy Django project documentation - Update
  README.md with automated release info and Docker image links - Update legacy release documentation
  with migration information - Provide reusable workflow guides for other Django projects


## v2.0.1 (2025-08-16)


## v2.0.1-a.1 (2025-08-16)

### Bug Fixes

- **ci**: Ensure Docker builds for main branch even without new releases
  ([`7ce789f`](https://github.com/dkdndes/cowboy-django/commit/7ce789f168d8870ef7e967cf73165f26de2e3e8a))

- Always build Docker images when main branch workflows complete - This ensures 'latest' tag is
  available for stable releases - Maintain existing logic for develop branch pre-releases

- **release**: Configure proper Django-style versioning
  ([`eeb69c9`](https://github.com/dkdndes/cowboy-django/commit/eeb69c93dea5cbb9e1d629e9322cf4ba5c44e141))

- Set develop branch to create pre-releases with 'a' token (v1.2.0a1) - Keep main branch for stable
  releases (v1.2.0) - Follow Django's official release process conventions


## v2.0.0 (2025-08-16)

### Bug Fixes

- **ci**: Pin semantic-release plugin versions to resolve parser errors
  ([`fdbc047`](https://github.com/dkdndes/cowboy-django/commit/fdbc047361b5c48155980784dfd1d5fa9f319a93))

Use known working versions instead of latest to fix the load-parser-config error: -
  semantic-release@22.0.12 - commit-analyzer@11.1.0 - Other plugins pinned to compatible versions

This should resolve the parser function compatibility issue.

- **ci**: Use default conventionalcommits rules to avoid parser errors
  ([`cbcd3f5`](https://github.com/dkdndes/cowboy-django/commit/cbcd3f55e02c47326585ebf1212ed7545b22cfe6))

Remove custom releaseRules that were causing semantic-release parser failures. Use default
  conventionalcommits behavior which should handle feat/fix correctly.

- **ci**: Remove problematic parserOpts from semantic-release config
  ([`177d4da`](https://github.com/dkdndes/cowboy-django/commit/177d4da7e748f7990c1c0903ecdf3232ce0d176d))

The parserOpts configuration was causing a parsing error in semantic-release. Use default parser
  options which handle BREAKING CHANGE correctly.

- **ci**: Repair semantic-release configuration for any repository (#20)
  ([#21](https://github.com/dkdndes/cowboy-django/pull/21),
  [`08a9d49`](https://github.com/dkdndes/cowboy-django/commit/08a9d498fa34f3d1933b20a952cd7dd71643d076))

- Add missing tagFormat to both release configs for consistent v1.2.3 tags - Use GitHub environment
  variables instead of hardcoded repository URLs - Fix semantic-release config path resolution with
  proper ./ prefix - Standardize release rules across develop and main configurations - Add
  comprehensive CLAUDE.md documentation for future development

This makes the release workflow portable to any Django project.

- **ignore**: Resolve .gitignore conflict and exclude CLAUDE.md from tracking
  ([`4332da8`](https://github.com/dkdndes/cowboy-django/commit/4332da86cd24d5a348ca598832df237b13b063f5))

- Resolve merge conflict in .gitignore - Add CLAUDE.md to .gitignore to keep it local only - Add
  explicit CLAUDE.md entry to .dockerignore for clarity - Remove conflicting nodejs entries leftover
  from migration

### Features

- **release**: Enable real releases and simplify semantic-release config
  ([`bbeb55e`](https://github.com/dkdndes/cowboy-django/commit/bbeb55ebdc8ecc873c8f054f0f4b225073dd58eb))

- Disable DRY_RUN mode by setting repository variable to false - Use default presets for
  commit-analyzer to avoid parser errors - This should trigger semantic-release to create v1.1.0
  based on feat commits

BREAKING CHANGE: This enables real releases instead of dry-run mode


## v1.2.1 (2025-08-16)

### Bug Fixes

- **ci**: Adopt working Docker login pattern from pybiorythm
  ([`1ee612b`](https://github.com/dkdndes/cowboy-django/commit/1ee612b9f43a2d82286e133906eeffe8247eaaa9))

- Use docker/login-action@v3 instead of manual docker login - Add security-events: write permission
  - Use standard github.repository instead of custom naming - Match proven working configuration
  from pybiorythm repository

This should resolve the 'permission_denied: write_package' error.


## v1.2.0 (2025-08-16)

### Features

- **ci**: Separate semantic-release and Docker workflows
  ([`1de720f`](https://github.com/dkdndes/cowboy-django/commit/1de720f330c92e07a7389f44f4daa7f4cef8d679))

- Split python-release.yml into semantic-release only workflow - Create docker-publish.yml workflow
  triggered by semantic-release completion - Use workflow_run trigger to pass version information
  between workflows - Add comprehensive labels and metadata to Docker images - Support both main and
  develop branch workflows

This separation allows: - Independent debugging of semantic-release vs Docker issues - Better
  control over Docker publishing permissions - Cleaner workflow outputs and summaries


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

- **lockfile**: Update package-lock.json for semantic-release setup
  ([`0f13f56`](https://github.com/dkdndes/cowboy-django/commit/0f13f56d17770d3ab4e07867b6318190b331c12d))

- **deps**: Add semantic-release toolchain and config to package.json
  ([`cab5ac1`](https://github.com/dkdndes/cowboy-django/commit/cab5ac15317ba0632454d331b2803a1a6baeab45))

- Ignore node_modules
  ([`7464c14`](https://github.com/dkdndes/cowboy-django/commit/7464c14eb95161fb90fb84e5268810c20a3ccb40))

Signed-off-by: PR <dkdndes@gmail.com>

- Ruff fix and ruff format
  ([`dfe8d9b`](https://github.com/dkdndes/cowboy-django/commit/dfe8d9b5b24cc0b568f64fadcb09099fe720df0a))

- Ruff fix and ruff format
  ([`8d4ceae`](https://github.com/dkdndes/cowboy-django/commit/8d4ceae7c49336e3c7f35bcabc4b0b4fa5e4de83))

### Documentation

- Ignore nodes_moduls
  ([`2dbd9a4`](https://github.com/dkdndes/cowboy-django/commit/2dbd9a4bd36fff874dc7cf688cb92d3765afd2ea))

- **release**: Add documentation for semantic-release and docker workflows
  ([`778fa8b`](https://github.com/dkdndes/cowboy-django/commit/778fa8b930851068db649c27d6916def4ed1b105))

### Features

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

- **ci**: Add local dry-run release workflow for act testing
  ([`0a1ca1d`](https://github.com/dkdndes/cowboy-django/commit/0a1ca1d7fdb77cb70a3b74ac52337a36a315b1f7))

- **ci**: Add release workflow for develop and main
  ([`b0fecc5`](https://github.com/dkdndes/cowboy-django/commit/b0fecc5e87641ad798ff3afe39b3e03105463011))


## v1.0.0 (2025-08-14)

### Documentation

- Update issue templates
  ([`e9a0df3`](https://github.com/dkdndes/cowboy-django/commit/e9a0df3c449d928b05aeb10ea48f2499bbb09347))

- Add comprehensive documentation and MIT license
  ([`b9a4064`](https://github.com/dkdndes/cowboy-django/commit/b9a406415988817bf31a89f7019e41333eff5cb1))

- Complete README with setup instructions - Docker standalone and local development guides -
  Detailed Kubernetes deployment workflow - Project structure and technical highlights - MIT license
  for open source distribution - Future extension roadmap

### Features

- Comprehensive readme
  ([`899cc46`](https://github.com/dkdndes/cowboy-django/commit/899cc4612040d65841e073343128a7c1c6608ab7))

- Add Kubernetes deployment manifests
  ([`f10505b`](https://github.com/dkdndes/cowboy-django/commit/f10505b82c2abea757489cc604f66aca971d29f0))

- Complete K8s manifests with namespace isolation - Init containers for automatic database
  migrations - ClusterIP service configuration - Resource limits and requests - Example nginx
  deployment for testing - Production-ready cowboy namespace setup

- Add Docker containerization with uv
  ([`b09c7c7`](https://github.com/dkdndes/cowboy-django/commit/b09c7c7ea3eb7ab3914d5242e11c1de53988ec0d))

- Multi-stage Docker build optimized for production - Modern uv dependency management integration -
  Proper .dockerignore for optimized build context - ASGI/Uvicorn server configuration - Container
  runs on port 8000

- Add core Django application with ASCII cowboy jokes
  ([`13d84ef`](https://github.com/dkdndes/cowboy-django/commit/13d84ef3364e3f1498256da573e04f16c1061327))

- Django 5.0+ application with HTMX frontend - ASCII art cowboys with Kubernetes-themed humor -
  JSON-based ASCII art storage (prevents Python syntax issues) - Session-based joke/art rotation
  system - Modern uv dependency management - Dark theme responsive design
