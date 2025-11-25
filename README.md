# ToBox Service

A well-structured FastAPI service with modular architecture.

## 📁 Project Structure

```
ToBox-Service/
├── app/                    # Application code
│   ├── api/               # API endpoints
│   │   └── v1/           # API version 1
│   │       ├── __init__.py
│   │       └── hello.py  # Hello endpoints
│   ├── core/             # Core functionality
│   │   ├── __init__.py
│   │   └── config.py     # Configuration management
│   ├── models/           # Database models (SQLAlchemy)
│   ├── schemas/          # Pydantic schemas
│   │   ├── __init__.py
│   │   └── hello.py      # Hello schemas
│   ├── services/         # Business logic
│   ├── utils/            # Utility functions
│   │   ├── __init__.py
│   │   └── logger.py     # Logging utilities
│   ├── __init__.py
│   └── main.py           # FastAPI application
├── tests/                # Test suite
│   ├── api/             # API tests
│   │   └── test_hello.py
│   ├── unit/            # Unit tests
│   └── conftest.py      # Pytest configuration
├── logs/                # Application logs
├── .env.example         # Environment variables example
├── .gitignore          # Git ignore rules
├── .python-version     # Python version
├── pyproject.toml      # Project dependencies
├── run.py              # Application entry point
└── README.md           # This file
```

## 🚀 Requirements

- Python 3.8+
- uv (Python package manager)

## 📦 Installation

1. Install uv if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository:
```bash
git clone git@github.com:lossercode/ToBox-Service.git
cd ToBox-Service
```

3. Install dependencies:
```bash
uv sync
```

4. Copy environment variables (optional):
```bash
cp .env.example .env
```

## 🏃 Running the Service

### Method 1: Using the run script (recommended)
```bash
uv run python run.py
```

### Method 2: Using uvicorn directly
```bash
uv run uvicorn app.main:app --reload
```

### Method 3: With custom host and port
```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The service will start on `http://localhost:8000`

## 📚 API Endpoints

### Root Endpoints
- `GET /` - Root endpoint with service info
- `GET /health` - Health check endpoint

### Hello Endpoints (v1)
- `GET /api/v1/hello` - Simple hello endpoint
- `GET /api/v1/hello/{name}` - Hello endpoint with name parameter

## 📖 API Documentation

Once the service is running, you can access:
- **Swagger UI**: http://localhost:8000/api/v1/docs
- **ReDoc**: http://localhost:8000/api/v1/redoc
- **OpenAPI JSON**: http://localhost:8000/api/v1/openapi.json

## 🧪 Testing

Run all tests:
```bash
uv run pytest
```

Run tests with coverage:
```bash
uv run pytest --cov=app tests/
```

Run specific test file:
```bash
uv run pytest tests/api/test_hello.py
```

## 🔧 Configuration

Configuration is managed through environment variables. See `.env.example` for available options:

- `PROJECT_NAME`: Project name
- `VERSION`: API version
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `DEBUG`: Debug mode (default: True)
- `API_V1_STR`: API v1 prefix (default: /api/v1)

## 📝 Development

### Adding a new endpoint

1. Create a new router file in `app/api/v1/`
2. Define your endpoints using FastAPI router
3. Create corresponding schemas in `app/schemas/`
4. Register the router in `app/api/v1/__init__.py`
5. Add tests in `tests/api/`

### Project Guidelines

- Follow PEP 8 style guide
- Use type hints for all functions
- Write docstrings for all public functions
- Add tests for new features
- Keep business logic in `services/`
- Use Pydantic models for request/response validation

## 📄 License

MIT License

## 👤 Author

lossercode (2790372069@qq.com)
