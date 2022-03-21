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

- export environment variables (sample of them available on file .env_sample)
- docker-compose up
- docker-compose exec employee_list python manage.py migrate
