# Cowboy Django Project Documentation

This document provides comprehensive information about the Cowboy Django project - a Django + HTMX web application that serves ASCII art cowboys with Kubernetes-themed jokes.

## Project Overview

Cowboy Django is a fun, educational web application designed for DevOps engineers and developers working with Kubernetes. It combines classic ASCII art aesthetics with modern web technologies and cloud-native deployment practices.

### Key Features

- **ASCII Art Cowboys**: Hand-crafted ASCII art displaying various cowboy characters
- **Kubernetes Humor**: Witty one-liners and jokes about pods, services, clusters, and cloud-native concepts
- **HTMX Interactivity**: Modern, responsive user interface without heavy JavaScript frameworks
- **Container-Ready**: Optimized Docker setup with modern Python tooling
- **Kubernetes-Native**: Production-ready Kubernetes manifests
- **Session-Based Rotation**: Deterministic cycling through art and joke combinations

## Architecture

### Technology Stack

- **Backend**: Django 5.0+ with ASGI/Uvicorn for async support
- **Frontend**: HTMX + Vanilla CSS for reactive UI
- **Dependency Management**: uv for fast, reliable Python package management
- **Containerization**: Docker with multi-stage builds
- **Orchestration**: Kubernetes with proper namespace isolation
- **Data Storage**: JSON-based ASCII art with SQLite (development) / PostgreSQL (production)

### Application Structure

```
cowboy-django/
├── asciiapp/                 # Main Django application
│   ├── ascii_arts.json      # ASCII art data store
│   ├── cowboy.py            # Art rendering and joke logic
│   ├── models.py            # Django models (minimal)
│   ├── views.py             # API endpoints and business logic
│   ├── urls.py              # URL routing
│   └── templates/asciiapp/  # HTMX templates
│       ├── base.html        # Base template with HTMX setup
│       └── cowboy.html      # Main application interface
├── cowboysite/              # Django project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL configuration
│   ├── asgi.py              # ASGI application
│   └── wsgi.py              # WSGI application (fallback)
├── .github/workflows/       # CI/CD automation
│   ├── python-release.yml   # Semantic release automation
│   └── docker-publish.yml   # Docker image publishing
├── docs/                    # Documentation
├── k8s.yaml                 # Kubernetes deployment manifests
├── Dockerfile               # Container definition
├── pyproject.toml           # Python project configuration
├── uv.lock                  # Dependency lock file
└── manage.py                # Django management script
```

## Core Components

### ASCII Art System

The ASCII art system is built around a JSON data structure containing pre-drawn cowboy art:

```json
[
  "\\n           ,'-',\\n          :-----:\\n     .'---'.  )    )\\n    /       \\/     /\\n   |    0     0   /\\n    \\   \\  ^  /  /\\n     )  ')-=-('  (\\n    /  /       \\  \\\\n   (  /         \\  )\\n    \\/           \\/\\n",
  "\\n    .-.\\n   (o o)\\n  /  V  \\\\n /|    |\\\\n/ |    | \\\\n  |    |\\n  |    |\\n  |    |\\n"
]
```

#### Features:
- **Deterministic Selection**: Uses session-based rotation to ensure users see different combinations
- **Scalable Storage**: JSON format allows easy addition of new art
- **Efficient Rendering**: Pre-processed strings for fast display

### Joke System

Kubernetes-themed humor system with categories:

```python
JOKES = [
    "Our cowboy lassoed some pods — now they're in a proper cluster!",
    "Why don't cowboys like microservices? Too many moving cattle!",
    "Pod went missing from the ranch — turned out to be a Job all along.",
    "This cowboy's got 99 problems, but a pod ain't one.",
    "Heard about the cowboy who automated his ranch? Now it's all serverless cattle!",
    # ... more jokes
]
```

#### Categories:
- **Pod Management**: Jokes about Kubernetes pods and containers
- **Cluster Operations**: Humor about cluster management and scaling
- **DevOps Culture**: General cloud-native and automation humor
- **Western Themes**: Cowboy metaphors for technical concepts

### HTMX Integration

Modern, lightweight interactivity using HTMX:

```html
<!-- Main application interface -->
<div id="cowboy" hx-get="/api/cowboy" hx-trigger="load">
    Loading cowboy wisdom...
</div>

<button hx-get="/api/cowboy" 
        hx-target="#cowboy" 
        hx-swap="innerHTML"
        class="btn">
    Get New Cowboy Wisdom
</button>
```

#### Benefits:
- **No JavaScript Frameworks**: Reduces bundle size and complexity
- **Server-Side Rendering**: Better SEO and initial load times
- **Progressive Enhancement**: Works without JavaScript, enhanced with it
- **Easy Maintenance**: Simple templating without complex state management

## Development Workflow

### Local Development Setup

1. **Clone and Setup**:
```bash
git clone https://github.com/dkdndes/cowboy-django.git
cd cowboy-django
```

2. **Install Dependencies**:
```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

3. **Database Setup**:
```bash
uv run python manage.py migrate
```

4. **Run Development Server**:
```bash
uv run python manage.py runserver
```

### Adding New Content

#### Adding ASCII Art
1. Create or find ASCII art (ensure it's properly escaped for JSON)
2. Add to `asciiapp/ascii_arts.json`
3. Test with the application

#### Adding Jokes
1. Edit `asciiapp/views.py`
2. Add to the `JOKES` list
3. Follow the Kubernetes/DevOps theme
4. Test in the application

#### Example New Joke:
```python
JOKES = [
    # ... existing jokes
    "Why did the cowboy's deployment fail? He forgot to wrangle his ConfigMaps!",
]
```

### Testing

#### Manual Testing
```bash
# Run Django tests
uv run python manage.py test

# Compile Python files for syntax check
uv run python -m py_compile asciiapp/*.py

# Check code style
uv run ruff check
uv run ruff format
```

#### Integration Testing
```bash
# Test with Docker
docker build -t cowboy-test .
docker run -p 8000:8000 cowboy-test

# Test Kubernetes deployment
kubectl apply -f k8s.yaml --dry-run=client
```

## Deployment Options

### Docker Deployment

#### Using Pre-built Images
```bash
# Latest stable
docker run -p 8000:8000 ghcr.io/dkdndes/cowboy-django:latest

# Development version
docker run -p 8000:8000 ghcr.io/dkdndes/cowboy-django:develop

# Specific version
docker run -p 8000:8000 ghcr.io/dkdndes/cowboy-django:v2.0.1
```

#### Building Locally
```bash
docker build -t cowboy-django .
docker run -p 8000:8000 cowboy-django
```

### Kubernetes Deployment

#### Prerequisites
- Kubernetes cluster (KIND, minikube, or cloud)
- kubectl configured
- Docker for image management

#### Deployment Steps
```bash
# For KIND clusters
docker pull ghcr.io/dkdndes/cowboy-django:latest
kind load docker-image ghcr.io/dkdndes/cowboy-django:latest

# Deploy application
kubectl apply -f k8s.yaml

# Check deployment
kubectl get all -n cowboy

# Access application
kubectl port-forward svc/cowboy-django -n cowboy 8000:80
```

#### Kubernetes Architecture
- **Namespace**: `cowboy` - Isolates all resources
- **Deployment**: `cowboy-django` - Main application with init containers
- **Service**: `cowboy-django` - ClusterIP service on port 80
- **Init Container**: Handles database migrations automatically
- **Resource Limits**: CPU and memory constraints for production

## Configuration

### Environment Variables

The application supports the following environment variables:

```bash
# Django settings
DEBUG=False                    # Production mode
SECRET_KEY=your-secret-key    # Django secret key
ALLOWED_HOSTS=localhost,127.0.0.1  # Allowed hostnames

# Database (for production)
DATABASE_URL=postgresql://user:pass@host:port/db

# Container settings
PORT=8000                     # Server port
```

### Django Settings

Key settings in `cowboysite/settings.py`:

```python
# ASGI/Uvicorn configuration
ASGI_APPLICATION = 'cowboysite.asgi.application'

# Static files (for production)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Security settings
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
```

## Performance Considerations

### Optimization Strategies

1. **Static File Serving**: Use CDN or nginx for static assets in production
2. **Database Optimization**: Migrate to PostgreSQL for production workloads
3. **Caching**: Implement Redis caching for frequently accessed data
4. **Container Optimization**: Multi-stage Docker builds reduce image size

### Scaling

#### Horizontal Scaling
```bash
# Scale Kubernetes deployment
kubectl scale deployment cowboy-django --replicas=3 -n cowboy

# Add load balancing
kubectl expose deployment cowboy-django --type=LoadBalancer -n cowboy
```

#### Vertical Scaling
```yaml
# In k8s.yaml - adjust resource requests/limits
resources:
  requests:
    memory: "128Mi"
    cpu: "250m"
  limits:
    memory: "256Mi"
    cpu: "500m"
```

## Production Considerations

### Security

1. **Secret Management**: Use Kubernetes Secrets for sensitive data
2. **TLS Configuration**: Implement HTTPS with cert-manager
3. **Database Security**: Use managed database services with encryption
4. **Container Security**: Regular image scanning and updates

### Monitoring

1. **Health Checks**: Kubernetes liveness and readiness probes
2. **Logging**: Centralized logging with ELK stack or cloud solutions
3. **Metrics**: Prometheus and Grafana for application metrics
4. **Alerting**: Set up alerts for deployment issues

### Backup and Recovery

1. **Database Backups**: Regular database snapshots
2. **Configuration Backup**: Version control for all configuration
3. **Image Registry**: Maintain multiple image versions
4. **Disaster Recovery**: Multi-region deployment strategies

## Troubleshooting

### Common Issues

**Application won't start:**
- Check Python dependencies with `uv sync`
- Verify Django settings configuration
- Check database connectivity

**HTMX not working:**
- Verify HTMX CDN link in templates
- Check browser console for JavaScript errors
- Ensure API endpoints return correct content types

**Kubernetes deployment fails:**
- Check image availability: `docker pull ghcr.io/dkdndes/cowboy-django:latest`
- Verify Kubernetes cluster connectivity: `kubectl cluster-info`
- Check resource constraints and node capacity

**Docker build fails:**
- Verify Dockerfile syntax
- Check base image availability
- Ensure all COPY sources exist

### Debug Commands

```bash
# Django debugging
uv run python manage.py check
uv run python manage.py shell

# Docker debugging
docker logs container-name
docker exec -it container-name /bin/bash

# Kubernetes debugging
kubectl logs deployment/cowboy-django -n cowboy
kubectl describe pod -l app=cowboy-django -n cowboy
kubectl exec -it deployment/cowboy-django -n cowboy -- /bin/bash
```

## Contributing

### Code Style

- Follow PEP 8 for Python code
- Use Django best practices
- Write descriptive commit messages
- Add tests for new functionality

### Contribution Process

1. Fork the repository
2. Create a feature branch
3. Add your improvements (jokes, art, features)
4. Test thoroughly
5. Submit a pull request
6. Engage in code review process

### Types of Contributions

- **New ASCII Art**: Add to the art collection
- **More Jokes**: Kubernetes/DevOps themed humor
- **Feature Enhancements**: New functionality
- **Documentation**: Improve guides and docs
- **Bug Fixes**: Resolve issues and improve stability

## Future Roadmap

### Planned Features

1. **Interactive Features**: User voting on jokes and art
2. **REST API**: Programmatic access to jokes and art
3. **Joke Submission**: Community-driven content
4. **Multiple Themes**: Different ASCII art categories
5. **Analytics**: Usage statistics and popular content
6. **Slack/Discord Integration**: Bot integration for team channels

### Technical Improvements

1. **Performance**: Caching layer and database optimization
2. **Accessibility**: WCAG compliance and screen reader support
3. **Internationalization**: Multi-language support
4. **Progressive Web App**: Offline functionality
5. **Real-time Features**: WebSocket integration for live updates

This project serves as both entertainment and a practical example of modern Django development practices, containerization, and Kubernetes deployment patterns. It demonstrates how to build, test, and deploy cloud-native applications while maintaining simplicity and fun.