#!/bin/bash

cd /home/site/wwwroot
echo "Moved to home/site/wwwroot directory..."

# Extract the tar.gz file
tar -xzf output.tar.gz

# Optional: remove it after extraction
# rm output.tar.gz

echo "Activating virtual environment..."
source antenv/bin/activate

echo "Starting Django app..."
#exec gunicorn phora_API.wsgi:application --bind=0.0.0.0 --timeout 600
exec python manage.py runserver 0.0.0.0:8000