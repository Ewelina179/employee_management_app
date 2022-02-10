import pytest

from employees.models import Employee

@pytest.mark.django_db
def test_employee_in_db(employee):
    employee_in = Employee.objects.get(first_name = "Jan", last_name = "Nowak")
    assert employee == employee_in

@pytest.mark.django_db
def test_change_employee(employee):
    employee.name = "Aleksander"
    employee.save()
    assert employee.name == "Aleksander"