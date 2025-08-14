FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Install uv using pip (best practice)
RUN pip install uv

# Copy everything including local .venv
COPY . .

# Use uv from local venv  
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "cowboysite.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
