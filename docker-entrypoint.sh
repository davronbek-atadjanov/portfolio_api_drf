#!/bin/bash

python manage.py migrate

# Collect static files
python manage.py collectstatic

# Start server
gunicorn core.wsgi:application --bind 0.0.0.0:8000
exec "$@"
