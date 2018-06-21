#!/bin/bash

docker exec -it golden-greyhound python manage.py dumpdata > backups/$(date "+%Y-%m-%dT%H:%M:%S").json