# Python FastAPI UV Application

A modern FastAPI application built with the UV package manager, featuring a complete REST API for managing items.

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **UV Package Manager**: Fast Python package installer and resolver
- **Pydantic Models**: Data validation and serialization
- **Auto-generated Documentation**: Interactive API docs with Swagger UI
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Health Check**: Built-in health monitoring endpoint
- **Search Functionality**: Search items by name

## API Endpoints

### Core Endpoints
- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

### Item Management
- `GET /items` - Get all items
- `GET /items/{item_id}` - Get a specific item by ID
- `POST /items` - Create a new item
- `PUT /items/{item_id}` - Update an existing item
- `DELETE /items/{item_id}` - Delete an item
- `GET /items/search/{name}` - Search items by name

## Data Models

### Item Model
```json
{
  "id": 1,
  "name": "Sample Item",
  "description": "A sample item description",
  "price": 29.99,
  "is_available": true
}
```

### Item Update Model
```json
{
  "name": "Updated Item Name",
  "description": "Updated description",
  "price": 39.99,
  "is_available": false
}
```

## Installation & Setup

### Prerequisites
- Python 3.11 or higher
- UV package manager

### Complete Installation Guide

#### 1. Install Python
First, ensure you have Python 3.11 or higher installed on your system.

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- Or use winget: `winget install Python.Python.3.11`

**macOS:**
- Download from [python.org](https://www.python.org/downloads/)
- Or use Homebrew: `brew install python@3.11`

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-pip
```

**Linux (CentOS/RHEL/Fedora):**
```bash
sudo dnf install python3.11 python3.11-pip
```

Verify installation:
```bash
python --version
# or
python3 --version
```

#### 2. Install Uvicorn
```bash
pip install uvicorn
```

#### 3. Install UV Package Manager
```bash
pip install uv
```

#### 4. Create Project Directory
```bash
mkdir python-fast-api-uv && cd python-fast-api-uv
```

#### 5. Initialize UV Project
```bash
uv init
```

#### 6. Add FastAPI with Standard Extras
```bash
uv add fastapi --extra standard
```

#### 7. Install Dependencies
```bash
uv sync
```

#### 8. Run the Application

**Development Mode:**
```bash
uv run fastapi dev
```

**Alternative Development Commands:**
```bash
uv run python main.py
```

Or:
```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Production Mode:**
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

### Quick Start (If Repository Already Exists)
If you're cloning an existing repository:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd python-fast-api-uv
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

3. **Run the application**:

   **Development Mode:**
   ```bash
   uv run fastapi dev
   ```

   **Alternative Development Commands:**
   ```bash
   uv run python main.py
   ```

   **Production Mode:**
   ```bash
   uv run uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Usage Examples

### Using curl

1. **Create an item**:
   ```bash
   curl -X POST "http://localhost:8000/items" \
        -H "Content-Type: application/json" \
        -d '{"name": "Laptop", "description": "High-performance laptop", "price": 999.99}'
   ```

2. **Get all items**:
   ```bash
   curl -X GET "http://localhost:8000/items"
   ```

3. **Get a specific item**:
   ```bash
   curl -X GET "http://localhost:8000/items/1"
   ```

4. **Update an item**:
   ```bash
   curl -X PUT "http://localhost:8000/items/1" \
        -H "Content-Type: application/json" \
        -d '{"price": 899.99}'
   ```

5. **Delete an item**:
   ```bash
   curl -X DELETE "http://localhost:8000/items/1"
   ```

6. **Search items**:
   ```bash
   curl -X GET "http://localhost:8000/items/search/laptop"
   ```

### Using the Interactive Documentation

1. Start the application
2. Open your browser and go to `http://localhost:8000/docs`
3. Use the Swagger UI to test all endpoints interactively

## Development

### Project Structure
```
python-fast-api-uv/
├── main.py          # Main FastAPI application
├── pyproject.toml   # Project configuration and dependencies
├── uv.lock         # Locked dependency versions
└── README.md       # This file
```

### Adding New Features

1. **Add new endpoints** in `main.py`
2. **Create new Pydantic models** for data validation
3. **Update dependencies** in `pyproject.toml` if needed
4. **Run `uv sync`** to update dependencies

### Testing

The application includes built-in testing capabilities through the interactive documentation. For automated testing, consider adding:

- `pytest` for unit tests
- `httpx` for API testing
- `pytest-asyncio` for async test support

## Production Deployment

For production deployment, consider:

1. **Database Integration**: Replace in-memory storage with a proper database (PostgreSQL, MongoDB, etc.)
2. **Authentication**: Add JWT or OAuth2 authentication
3. **Environment Variables**: Use environment variables for configuration
4. **Docker**: Containerize the application
5. **Reverse Proxy**: Use Nginx or similar for production serving
6. **Monitoring**: Add logging and monitoring solutions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues, please open an issue in the repository or contact the maintainers.
