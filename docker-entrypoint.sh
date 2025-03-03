#!/bin/bash

python manage.py migrate

# Start server
#gunicorn core.wsgi:application --bind 0.0.0.0:8000
exec "$@"
