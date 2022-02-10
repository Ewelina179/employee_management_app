import pytest

from employees.models import Employee

@pytest.fixture(scope='session')
def employee_first(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        return Employee.objects.create(first_name="Jan", last_name="Nowak", age="33", profession="teacher")

@pytest.fixture(scope='session')
def employee_second(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        return Employee.objects.create(first_name="Jan", last_name="Nowak", age="25", profession="data analyst")

@pytest.fixture(scope='session')
def employee_third(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        return Employee.objects.create(first_name="Jan", last_name="Nowak", age="43", profession="teacher")