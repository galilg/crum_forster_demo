#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn
exec gunicorn crum_forster.wsgi:application\
    --bind 0.0.0.0:8878 \
    --workers 3
