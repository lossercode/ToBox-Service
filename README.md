# ToBox Service
A simple FastAPI service with hello endpoint.

## Requirements

- Python 3.8+
- uv (Python package manager)

## Installation

1. Install uv if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Install dependencies:
```bash
uv sync
```

## Running the Service

### Using uvicorn directly:
```bash
uv run uvicorn main:app --reload
```

### Or run the main.py file:
```bash
uv run python main.py
```

The service will start on `http://localhost:8000`

## API Endpoints

- `GET /` - Root endpoint
- `GET /hello` - Simple hello endpoint
- `GET /hello/{name}` - Hello endpoint with name parameter

## API Documentation

Once the service is running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
