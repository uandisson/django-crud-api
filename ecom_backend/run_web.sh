#!/usr/bin/env bash


python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py runserver 8000
