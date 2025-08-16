# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Local Development with uv
```bash
# Install dependencies
uv sync

# Run database migrations
uv run python manage.py migrate

# Start development server
uv run python manage.py runserver

# Run tests
uv run python manage.py test

# Compile Python files
uv run python -m py_compile asciiapp/*.py

# Lint code
uv run ruff check
uv run ruff format
```

### Docker Development
```bash
# Build image
docker build -t dkdndes/cowboy-django .

# Run container
docker run -p 8000:8000 dkdndes/cowboy-django
```

### Kubernetes Deployment
```bash
# Deploy to cluster
kubectl apply -f k8s.yaml

# Monitor deployment
kubectl get pods -n cowboy
kubectl logs -f deployment/cowboy-django -n cowboy

# Access application
kubectl port-forward svc/cowboy-django -n cowboy 8000:80
```

### Release & Versioning
This project uses semantic-release with Conventional Commits:
- `feat(scope): description` → minor version bump
- `fix(scope): description` → patch version bump  
- `BREAKING CHANGE:` in commit body → major version bump

```bash
# Test release workflow locally with act
act push \
    -W .github/workflows/release-act-test.yml \
    -j build-release-dry-run \
    -P ubuntu-latest=catthehacker/ubuntu:act-latest \
    --container-architecture linux/amd64 \
    --pull=false \
    -e <(printf '{"ref":"refs/heads/feature/test-ci"}')
```

## Code and Commit Guidelines

### IMPORTANT: No AI References
- **NEVER** include references to yourself (you the AI) in source code, comments, commit messages, or documentation
- **NEVER** add something like "Generated with … Code" or similar attribution
- **NEVER** add something like "Co-Authored-By: …." in commits
- Keep all contributions stay as natural developer work

### Git Workflow
- Main branch: `main` (for releases)
- Development branch: `develop` (for ongoing work)
- Use conventional commits (feat:, fix:, docs:, etc.)
- Never work directly in main branch

## Architecture Overview

### Project Structure
- **asciiapp/**: Main Django app containing ASCII art logic
  - `ascii_arts.json`: JSON storage for ASCII art patterns
  - `cowboy.py`: Art rendering and text manipulation logic
  - `views.py`: API endpoints and Kubernetes-themed jokes
  - `templates/asciiapp/`: HTMX frontend templates
- **cowboysite/**: Django project configuration and settings
- **k8s.yaml**: Complete Kubernetes deployment manifest with namespace isolation
- **Dockerfile**: Multi-stage container build using uv for dependency management

### Technology Stack
- **Backend**: Django 5.0+ with ASGI/Uvicorn for async support
- **Frontend**: HTMX for dynamic updates with vanilla CSS
- **Dependencies**: Managed via uv (modern Python package manager)
- **Database**: SQLite (development), designed for PostgreSQL migration
- **Containerization**: Docker with init containers for migrations
- **Orchestration**: Kubernetes with dedicated namespace and services

### Key Components

#### Session-Based Rotation System
The app uses Django sessions to deterministically cycle through jokes and ASCII art:
- `_next_index()` function in `asciiapp/views.py:14` manages rotation state
- Resets on home page visits, continues on API calls
- Ensures users see all content before repeating

#### HTMX Integration
Frontend uses HTMX for seamless updates:
- `hx-get="/api/cowboy"` triggers content refresh
- Server returns pre-rendered HTML fragments
- No JavaScript frameworks required

#### Kubernetes-Native Design
- Deploys in `cowboy` namespace for resource isolation
- Init container handles database migrations automatically
- Service exposes on port 80 with ClusterIP type
- Ready for horizontal scaling and ingress configuration

### Development Patterns

#### Adding New Jokes
Edit the `JOKES` list in `asciiapp/views.py:5` - the rotation system handles the rest.

#### Adding ASCII Art
Add patterns to `asciiapp/ascii_arts.json` as escaped string literals. The app automatically pairs them with jokes based on index position.

#### Conventional Commits
Use structured commit messages for automatic versioning:
- feat(api): add new cowboy endpoint
- fix(ui): prevent double fetch on refresh  
- docs(readme): update deployment instructions

### CI/CD Integration
- **develop** branch: Auto-builds and pushes Docker images tagged as `:develop` and `:vX.Y.Z`
- **main** branch: Creates GitHub releases and pushes `:latest` and `:vX.Y.Z` tags
- **feature/** branches: Runs dry-run tests without publishing
- Uses GitHub Container Registry (GHCR) with OCI labels for proper repo association