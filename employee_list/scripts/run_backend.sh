#!/usr/bin/env bash

cd /employee_list/ && \
python ./manage.py migrate --no-input && \
python ./manage.py runserver 0.0.0.0:8000