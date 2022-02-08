import pytest

from employees.models import Employee

@pytest.fixture
def employee():
    return Employee.objects.create(first_name="Jan", last_name="Nowak", age="33", profession="teacher")

@pytest.mark.django_db
def test_employee_in_db(employee):
    employee_in = Employee.objects.get(first_name = "Jan", last_name = "Nowak")
    assert employee == employee_in