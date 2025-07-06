# Python FastAPI UV Application

A modern, production-ready FastAPI application built with the UV package manager, featuring a complete REST API for managing items with HTTPS support, comprehensive documentation, and best practices for development and deployment.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs with automatic OpenAPI documentation
- **UV Package Manager**: Fast Python package installer and resolver for dependency management
- **Pydantic Models**: Data validation and serialization with automatic type checking
- **Auto-generated Documentation**: Interactive API docs with Swagger UI and ReDoc
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality for items
- **Health Check**: Built-in health monitoring endpoint for production monitoring
- **Search Functionality**: Search items by name with case-insensitive matching
- **HTTPS Support**: SSL/TLS encryption with automatic certificate generation
- **Environment Configuration**: Flexible configuration via environment variables
- **Error Handling**: Comprehensive HTTP error responses with proper status codes
- **Async/Await**: Full async support for high-performance concurrent requests
- **Type Hints**: Complete type annotations for better code quality and IDE support

## 📋 API Endpoints

### Core Endpoints
| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| `GET` | `/` | Root endpoint with API information | JSON with API details and documentation links |
| `GET` | `/health` | Health check endpoint for monitoring | JSON with service status |
| `GET` | `/docs` | Interactive API documentation (Swagger UI) | HTML documentation interface |
| `GET` | `/redoc` | Alternative API documentation (ReDoc) | HTML documentation interface |

### Item Management Endpoints
| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| `GET` | `/items` | Get all items | - | Array of Item objects |
| `GET` | `/items/{item_id}` | Get a specific item by ID | - | Item object or 404 error |
| `POST` | `/items` | Create a new item | Item object (without ID) | Created Item object |
| `PUT` | `/items/{item_id}` | Update an existing item | ItemUpdate object | Updated Item object or 404 error |
| `DELETE` | `/items/{item_id}` | Delete an item | - | Success message or 404 error |
| `GET` | `/items/search/{name}` | Search items by name | - | Array of matching Item objects |

## 📊 Data Models

### Item Model
Complete item representation with all fields:

```json
{
  "id": 1,
  "name": "Sample Item",
  "description": "A sample item description",
  "price": 29.99,
  "is_available": true
}
```

**Field Descriptions:**
- `id` (Optional[int]): Unique identifier, auto-generated if not provided
- `name` (str): Item name (required)
- `description` (Optional[str]): Item description
- `price` (float): Item price in decimal format
- `is_available` (bool): Availability status, defaults to true

### Item Update Model
Partial update model allowing selective field updates:

```json
{
  "name": "Updated Item Name",
  "description": "Updated description",
  "price": 39.99,
  "is_available": false
}
```

**Field Descriptions:**
- All fields are optional for partial updates
- Only provided fields will be updated
- Maintains data integrity with existing values

## 🛠️ Installation & Setup

### Prerequisites
- **Python 3.11 or higher** - Required for modern Python features and type hints
- **UV package manager** - Fast Python package installer and resolver
- **OpenSSL** - For SSL certificate generation (optional, for HTTPS)

### Complete Installation Guide

#### 1. Install Python
First, ensure you have Python 3.11 or higher installed on your system.

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- Or use winget: `winget install Python.Python.3.11`
- Or use Chocolatey: `choco install python311`

**macOS:**
- Download from [python.org](https://www.python.org/downloads/)
- Or use Homebrew: `brew install python@3.11`
- Or use pyenv: `pyenv install 3.11.0`

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-pip
```

**Linux (CentOS/RHEL/Fedora):**
```bash
sudo dnf install python3.11 python3.11-pip
```

**Linux (Arch):**
```bash
sudo pacman -S python311
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

#### 4. Install OpenSSL (Optional, for HTTPS)
**Windows:**
- Download from [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html)
- Or use Chocolatey: `choco install openssl`

**macOS:**
```bash
brew install openssl
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt install openssl
```

**Linux (CentOS/RHEL/Fedora):**
```bash
sudo dnf install openssl
```

#### 5. Create Project Directory
```bash
mkdir python-fast-api-uv && cd python-fast-api-uv
```

#### 6. Initialize UV Project
```bash
uv init
```

#### 7. Add FastAPI with Standard Extras
```bash
uv add fastapi --extra standard
```

#### 8. Install Dependencies
```bash
uv sync
```

#### 9. Run the Application

**Development Mode (HTTP):**
```bash
uv run fastapi dev
```

**Development Mode (HTTPS):**
```bash
# Generate SSL certificates first (one-time setup)
uv run python main.py --generate-ssl

# Run with HTTPS
uv run python main.py
```

**Alternative Development Commands:**
```bash
uv run python main.py
```

Or:
```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Production Mode (HTTP):**
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

**Production Mode (HTTPS):**
```bash
# Set environment variables for your SSL certificates
export SSL_KEYFILE="/path/to/your/private.key"
export SSL_CERTFILE="/path/to/your/certificate.crt"

# Run with HTTPS
uv run uvicorn main:app --host 0.0.0.0 --port 8443 --ssl-keyfile $SSL_KEYFILE --ssl-certfile $SSL_CERTFILE
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

## 🔧 Usage Examples

### Using curl

#### HTTP Endpoints
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

#### HTTPS Endpoints (if using SSL)
1. **Create an item with HTTPS**:
   ```bash
   curl -X POST "https://localhost:8443/items" \
        -H "Content-Type: application/json" \
        -d '{"name": "Laptop", "description": "High-performance laptop", "price": 999.99}' \
        -k  # Skip certificate verification for self-signed certs
   ```

2. **Get all items with HTTPS**:
   ```bash
   curl -X GET "https://localhost:8443/items" -k
   ```

### Using Python requests

```python
import requests
import json

# Base URL (change to https://localhost:8443 for HTTPS)
base_url = "http://localhost:8000"

# Create an item
item_data = {
    "name": "Smartphone",
    "description": "Latest smartphone model",
    "price": 699.99,
    "is_available": True
}

response = requests.post(f"{base_url}/items", json=item_data)
print(f"Created item: {response.json()}")

# Get all items
response = requests.get(f"{base_url}/items")
items = response.json()
print(f"Total items: {len(items)}")

# Search items
response = requests.get(f"{base_url}/items/search/smartphone")
matching_items = response.json()
print(f"Found {len(matching_items)} matching items")
```

### Using JavaScript/Fetch

```javascript
const baseUrl = 'http://localhost:8000'; // Change to https://localhost:8443 for HTTPS

// Create an item
async function createItem(itemData) {
    const response = await fetch(`${baseUrl}/items`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(itemData)
    });
    return await response.json();
}

// Get all items
async function getItems() {
    const response = await fetch(`${baseUrl}/items`);
    return await response.json();
}

// Usage
createItem({
    name: "Wireless Headphones",
    description: "Noise-cancelling wireless headphones",
    price: 199.99
}).then(item => console.log('Created:', item));

getItems().then(items => console.log('All items:', items));
```

### Using the Interactive Documentation

1. **Start the application**:
   ```bash
   uv run python main.py
   ```

2. **Open your browser and navigate to**:
   - **HTTP**: `http://localhost:8000/docs`
   - **HTTPS**: `https://localhost:8443/docs`

3. **Use the Swagger UI to**:
   - View all available endpoints
   - Test API calls interactively
   - See request/response schemas
   - Try different parameters and request bodies

4. **Alternative documentation**:
   - **ReDoc**: `http://localhost:8000/redoc` or `https://localhost:8443/redoc`
   - **OpenAPI JSON**: `http://localhost:8000/openapi.json` or `https://localhost:8443/openapi.json`

## 🔒 HTTPS Configuration

### Self-Signed Certificates (Development)
For development, you can generate self-signed SSL certificates:

```bash
# Generate certificates (one-time setup)
uv run python main.py --generate-ssl
```

This will create:
- `certs/key.pem` - Private key (2048-bit RSA)
- `certs/cert.pem` - Self-signed certificate (valid for 365 days)

**Certificate Details:**
- **Subject**: `/C=US/ST=State/L=City/O=Organization/CN=localhost`
- **Key Size**: 2048 bits
- **Validity**: 365 days
- **Usage**: Development and testing only

### Production SSL Certificates
For production, use proper SSL certificates from a trusted Certificate Authority:

1. **Obtain certificates** from providers like:
   - [Let's Encrypt](https://letsencrypt.org/) (free)
   - [DigiCert](https://www.digicert.com/)
   - [Comodo](https://www.comodo.com/)
   - [GlobalSign](https://www.globalsign.com/)

2. **Set environment variables**:
   ```bash
   export SSL_KEYFILE="/path/to/your/private.key"
   export SSL_CERTFILE="/path/to/your/certificate.crt"
   ```

3. **Run with HTTPS**:
   ```bash
   uv run uvicorn main:app --host 0.0.0.0 --port 8443 --ssl-keyfile $SSL_KEYFILE --ssl-certfile $SSL_CERTFILE
   ```

### SSL Certificate Requirements
- **Private Key**: RSA or ECDSA private key file
- **Certificate**: X.509 certificate file
- **Format**: PEM format (base64 encoded)
- **Permissions**: Ensure proper file permissions (600 for private key)
- **Chain**: Include intermediate certificates if required

### Browser Security Warnings
When using self-signed certificates, browsers will show security warnings. This is normal for development. Click "Advanced" and "Proceed to localhost" to access your API.

### Testing HTTPS Endpoints
```bash
# Test with curl (skip certificate verification)
curl -k https://localhost:8443/health

# Test with Python requests
import requests
response = requests.get('https://localhost:8443/health', verify=False)
print(response.json())
```

## 🛠️ Development

### Project Structure
```
python-fast-api-uv/
├── main.py              # Main FastAPI application with HTTPS support
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock             # Locked dependency versions
├── .gitignore          # Git ignore rules
├── README.md           # This comprehensive documentation
└── certs/              # SSL certificates directory (auto-generated)
    ├── key.pem         # Private key (development)
    └── cert.pem        # Certificate (development)
```

### Adding New Features

1. **Add new endpoints** in `main.py`
2. **Create new Pydantic models** for data validation
3. **Update dependencies** in `pyproject.toml` if needed
4. **Run `uv sync`** to update dependencies
5. **Update documentation** in this README.md

### Testing

The application includes built-in testing capabilities through the interactive documentation. For automated testing, consider adding:

- `pytest` for unit tests
- `httpx` for API testing
- `pytest-asyncio` for async test support
- `pytest-cov` for coverage reporting

### Code Quality

- **Type Hints**: All functions include complete type annotations
- **Error Handling**: Comprehensive HTTP error responses
- **Documentation**: Auto-generated OpenAPI documentation
- **Validation**: Pydantic models for request/response validation

## 🚀 Production Deployment

### Environment Setup
1. **Database Integration**: Replace in-memory storage with a proper database
   - PostgreSQL with SQLAlchemy
   - MongoDB with motor
   - Redis for caching
   
2. **Authentication & Authorization**: Add security layers
   - JWT tokens with `python-jose`
   - OAuth2 with `python-multipart`
   - Role-based access control
   
3. **Environment Configuration**: Use environment variables
   ```bash
   export DATABASE_URL="postgresql://user:pass@localhost/db"
   export SECRET_KEY="your-secret-key"
   export DEBUG="false"
   ```

### Deployment Options

#### Docker Deployment
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install uv
RUN uv sync --frozen
EXPOSE 8000 8443
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Cloud Platforms
- **AWS**: ECS, Lambda, or EC2 with ALB
- **Google Cloud**: Cloud Run or GKE
- **Azure**: Container Instances or AKS
- **Heroku**: Direct deployment with Procfile

#### Reverse Proxy Setup
```nginx
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Monitoring & Logging
- **Application Logs**: Structured logging with `structlog`
- **Health Checks**: Built-in `/health` endpoint
- **Metrics**: Prometheus metrics with `prometheus-fastapi-instrumentator`
- **Tracing**: Distributed tracing with OpenTelemetry
- **Error Tracking**: Sentry integration for error monitoring

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** with proper type hints and documentation
4. **Add tests** if applicable
5. **Update documentation** in this README.md
6. **Submit a pull request** with a clear description

### Development Guidelines
- Follow PEP 8 style guidelines
- Include type hints for all functions
- Add docstrings for complex functions
- Test your changes thoroughly
- Update documentation as needed

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

### Getting Help
- **Documentation**: Check this README and the interactive API docs
- **Issues**: Open an issue in the repository for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas

### Common Issues
- **SSL Certificate Warnings**: Normal for self-signed certificates in development
- **Port Already in Use**: Change the port in the uvicorn command
- **Dependency Issues**: Run `uv sync` to refresh dependencies

### Contact
- **Repository**: [GitHub Issues](https://github.com/yourusername/python-fast-api-uv/issues)
- **Email**: your-email@example.com
- **Discord**: Join our community server

---

**Made with ❤️ using FastAPI and UV**
