#!/bin/bash

if [ $# -lt 1 ]
then
    echo $#
    echo "usage: ./make_models.sh <app_name>"
    exit 1
fi

python3 manage.py makemigrations $1
python3 manage.py migrate
