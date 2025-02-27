#!/bin/bash

# Migrate
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start server
echo "Starting server..."
gunicorn core.wsgi:application --bind 0.0.0.0:8000