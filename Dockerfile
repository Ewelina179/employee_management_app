FROM python:3

ENV PYTHONBUFFERED 1

WORKDIR /employee_list

COPY ./employee_list /employee_list

RUN pip install -r requirements.txt