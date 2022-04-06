import pytest

from employees.models import Employee, Profession

@pytest.fixture(scope='session')
def profession_teacher(django_db_setup, django_db_blocker):
     with django_db_blocker.unblock():
        return Profession.objects.create(name="teacher")


@pytest.fixture(scope='session')
def employee_first(django_db_setup, django_db_blocker, profession_teacher):
    with django_db_blocker.unblock():
        return Employee.objects.create(first_name="Jan", last_name="Nowak", age="33", profession=profession_teacher)

@pytest.fixture(scope='session')
def employee_second(django_db_setup, django_db_blocker, profession_teacher):
    with django_db_blocker.unblock():
        return Employee.objects.create(first_name="Jan", last_name="Nowak", age="25", profession=profession_teacher)

@pytest.fixture(scope='session')
def employee_negative(django_db_setup, django_db_blocker, profession_teacher):
    with django_db_blocker.unblock():
        return Employee.objects.create(first_name="Jan", last_name="Nowak", age="nie ma", profession=profession_teacher)

