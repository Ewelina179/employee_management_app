# employee_management_app

## Description

An application that allows to add, delete, update and display employees and creating reports about average age of the profession.

## Prerequisites and usage

- git clone
- cd employee_management_app\employee_list
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

## How to run application with docker-compose

- docker-compose --env-file ./config/.env.dev up (to set development environment variables)
