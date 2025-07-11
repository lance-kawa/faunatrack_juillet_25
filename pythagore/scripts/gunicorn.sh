#!/bin/sh
python manage.py migrate
gunicorn pythagore.wsgi:application --bind 0.0.0.0:8000 --log-level info --timeout 90  --access-logfile '-' --error-logfile '-'
