#!/bin/bash

# Migratsiyalarni bajarish
python manage.py makemigrations
python manage.py migrate

# Statik fayllarni to'plash
python manage.py collectstatic --noinput --clear

# Django serverini ishga tushurish
exec "$@"
