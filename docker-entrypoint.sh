#!/bin/bash

# Migratsiyalarni bajarish
python manage.py migrate

# Statik fayllarni to'plash
python manage.py collectstatic

# Django serverini ishga tushurish
exec "$@"
