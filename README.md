# Cowboy Django: Kubernetes Edition

A Django + HTMX web app that serves ASCII art cowboys with Kubernetes-themed jokes. Perfect for DevOps engineers who need a laugh between deployments!

**Repository**: [cowboy-django](https://github.com/dkdndes/cowboy-django)  
**Docker Images**: [ghcr.io/dkdndes/cowboy-django](https://github.com/users/dkdndes/packages/container/package/cowboy-django)  
**Latest Release**: ![GitHub release](https://img.shields.io/github/v/release/dkdndes/cowboy-django)

# What It Is

Cowboy Django is a fun web application that displays ASCII art cowboys delivering witty one-liners about Kubernetes, containers, and cloud-native technologies. Think cowsay but with a western theme and DevOps humor.

## Features

-	ASCII Art Cowboys – Beautiful hand-crafted ASCII art
-	Kubernetes Jokes – Clever puns about pods, services, and clusters
-	HTMX Interactivity – Smooth, fast page updates without JavaScript frameworks
-	Container Ready – Optimized Docker setup with uv dependency management
-	Kubernetes Native – Production-ready manifests with proper namespace organization
-	Session Rotation – Deterministic cycling through jokes and art

# Quick Start

## Option 1: Docker (Pre-built Images)

### Run latest stable release
```bash
docker run -p 8000:8000 ghcr.io/dkdndes/cowboy-django:latest
```

### Run development version
```bash
docker run -p 8000:8000 ghcr.io/dkdndes/cowboy-django:develop
```

### Run specific version
```bash
docker run -p 8000:8000 ghcr.io/dkdndes/cowboy-django:v2.0.1
```

Visit: http://localhost:8000

## Option 2: Docker (Build Locally)

### Clone the repository
```bash
git clone https://github.com/dkdndes/cowboy-django.git
cd cowboy-django
```

### Build and run locally
```bash
docker build -t cowboy-django .
docker run -p 8000:8000 cowboy-django
```

Visit: http://localhost:8000

## Option 3: Local Development with uv

### Clone and setup

```bash
git clone https://github.com/dkdndes/cowboy-django.git
cd cowboy-django
```
### Install dependencies
```
uv sync
```
### Run migrations

```
uv run python manage.py migrate
```
### Start development server

```
uv run python manage.py runserver
```
Visit: http://localhost:8000

# Automated Releases & Docker Images

This project uses automated workflows for releases and Docker image publishing:

## 🔄 Release Workflow
- **Develop branch** → Creates pre-releases (e.g., `v2.0.1-a.1`) for testing
- **Main branch** → Creates stable releases (e.g., `v2.0.1`) for production
- **Conventional commits** drive version bumps automatically

## 🐳 Docker Images
- **Latest stable**: `ghcr.io/dkdndes/cowboy-django:latest`
- **Development**: `ghcr.io/dkdndes/cowboy-django:develop`  
- **Specific versions**: `ghcr.io/dkdndes/cowboy-django:v2.0.1`
- **Pre-releases**: `ghcr.io/dkdndes/cowboy-django:v2.0.1-a.1`

## 📚 Workflow Documentation
For using these workflows in your own Django projects:
- [Python Semantic Release Workflow](docs/python-semantic-release-workflow.md)
- [Docker Build & Publish Workflow](docs/docker-build-publish-workflow.md)

# Kubernetes Deployment

Deploy to your Kubernetes cluster for sharing the cowboy wisdom with your team!

Prerequisites
	•	Kubernetes cluster (local KIND, minikube, or cloud cluster)
	•	kubectl configured
	•	Docker (for building images)

## Step-by-Step Deployment

### 1. Load Pre-built Image (for KIND)

```bash
# Pull latest stable release
docker pull ghcr.io/dkdndes/cowboy-django:latest

# Load into KIND cluster
kind load docker-image ghcr.io/dkdndes/cowboy-django:latest --name your-cluster-name
```

Or build locally:
```bash
docker build -t dkdndes/cowboy-django:latest .
kind load docker-image dkdndes/cowboy-django:latest --name your-cluster-name
```

### 2. Deploy to Kubernetes

```
kubectl apply -f k8s.yaml
kubectl get pods -n cowboy
kubectl get services -n cowboy
```

### 3. Access the Application

```
kubectl port-forward svc/cowboy-django -n cowboy 8000:80
```

Visit: http://localhost:8000

### 4. Monitor and Debug

```
kubectl logs -f deployment/cowboy-django -n cowboy
kubectl describe pod -l app=cowboy-django -n cowboy
kubectl scale deployment cowboy-django --replicas=3 -n cowboy
```

⸻

# Kubernetes Architecture

The app deploys in the cowboy namespace with:
-	Namespace: cowboy – Isolates all resources
-	Deployment: cowboy-django – Main application
-	Init Container: Handles database migrations automatically
-	Service: cowboy-django – ClusterIP service on port 80
-	Example Service: nginx-example – Additional nginx pods for testing

# Project Structure

```
cowboy-django/
├── asciiapp/               # Django app
│   ├── ascii_arts.json      # ASCII art data
│   ├── cowboy.py            # Art rendering logic
│   ├── urls.py              # App URL routing
│   ├── views.py             # API endpoints & K8s jokes
│   └── templates/asciiapp/  # HTMX frontend
├── cowboysite/              # Django project
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── k8s.yaml                 # Kubernetes manifests
├── Dockerfile               # Container definition
├── pyproject.toml           # uv dependencies
├── manage.py
├── LICENSE                  # MIT License
└── README.md
```


# Technology Stack

- Backend: Django 5.0+ with ASGI/Uvicorn
- Frontend: HTMX + Vanilla CSS
-	Dependencies: Managed with uv
- Containerization: Docker
-	Orchestration: Kubernetes
-	Data: JSON-based ASCII art storage


# Technical Highlights

## ASCII Art Storage

[
  "\\n           ,'-',\\n          :-----:\\n...",
  "\\n             ,\\n            /:\\\\n..."
]

## HTMX Integration

<div id="cowboy" hx-get="/api/cowboy" hx-trigger="load"></div>

## Kubernetes-Themed Humor

JOKES = [
    "Pod went missing — turned out to be a Job all along.",
    "Our cowboy lassoed nodes; now it's a proper cluster.",
]

## Modern Python Tooling

```
RUN pip install uv
COPY pyproject.toml uv.lock ./
COPY . .
CMD ["uv", "run", "uvicorn", "cowboysite.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
```

# Development

## Adding New Jokes

Edit asciiapp/views.py and add to the JOKES list.

## Adding New ASCII Art
	1.	Add to asciiapp/ascii_arts.json
	2.	The app automatically cycles through art/joke combinations

## Running Tests

```
uv run python manage.py test
uv run python -m py_compile asciiapp/*.py
```

# Production Considerations

- Migrate from SQLite to PostgreSQL
-	Configure static file serving
-	Store secrets in Kubernetes Secrets
-	Add autoscaling and monitoring
-	Configure ingress controller


# Future Extensions

- More joke categories
- Interactive features (voting, submissions)
- Slack/Matrix integration
-	REST API
-	ASCII art themes
-	Joke analytics

# Contributing

1.	Fork the repo
2.	Add your jokes or art
3.	Submit a PR
4.	Share the fun

# License

MIT License – see LICENSE

⸻

“In the wild west of Kubernetes, every cowboy needs a good laugh between deployments.”
