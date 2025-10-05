# Monitoring System

A Django-based monitoring system with a modern web interface.

## Features

- 🖥️ **System Monitoring**: Real-time monitoring of system resources and performance
- 📊 **Analytics Dashboard**: Interactive charts and comprehensive reporting
- 🔔 **Alert System**: Instant notifications for threshold breaches and issues
- 🛡️ **Health Checks**: RESTful API endpoints for system health monitoring
- 🎨 **Modern UI**: Responsive design with Bootstrap 5 and Font Awesome icons

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd monitoring
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main dashboard: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - Health check API: http://127.0.0.1:8000/api/health/

## Project Structure

```
monitoring/
├── apps/
│   └── core/           # Core application
│       ├── __init__.py
│       ├── apps.py
│       ├── urls.py
│       └── views.py
├── monitoring/         # Project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── templates/          # HTML templates
│   └── core/
│       └── home.html
├── static/             # Static files (CSS, JS, images)
├── media/              # User uploaded files
├── logs/               # Application logs
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
└── .gitignore         # Git ignore rules
```

## Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

- `SECRET_KEY`: Django secret key for security
- `DEBUG`: Enable/disable debug mode
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- Database settings (if using PostgreSQL)

### Database

By default, the project uses SQLite for development. For production, configure PostgreSQL:

1. Update database settings in `monitoring/settings.py`
2. Install PostgreSQL and create a database
3. Update environment variables in `.env`

## API Endpoints

### Health Check
- **GET** `/api/health/` - Returns system health status

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
The project follows PEP 8 guidelines. Consider using:
- `black` for code formatting
- `flake8` for linting
- `isort` for import sorting

### Adding New Features

1. Create a new Django app: `python manage.py startapp <app_name>`
2. Add the app to `INSTALLED_APPS` in `settings.py`
3. Create models, views, and URLs
4. Add URL patterns to the main `urls.py`

## Deployment

### Production Settings

1. Set `DEBUG=False` in production
2. Use a production database (PostgreSQL recommended)
3. Configure static file serving
4. Set up proper logging
5. Use environment variables for sensitive data

### Docker Deployment (Optional)

Create a `Dockerfile` and `docker-compose.yml` for containerized deployment.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For questions or issues, please open an issue on the GitHub repository.


