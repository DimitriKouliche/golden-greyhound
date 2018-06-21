#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput --clear

# Generating database migrations
echo "Generating database migrations"
python manage.py makemigrations enigma --no-input

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Load Data
echo "Loading Data"
python manage.py loaddata db.json

# Create Super User
echo "Creating Super User"
echo "from django.contrib.auth.models import User; User.objects.filter(email='d.kouliche@gmail.com').delete(); User.objects.create_superuser('Dimitri', 'd.kouliche@gmail.com', 'Bv9KHeK0HfI')" | python manage.py shell

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:80