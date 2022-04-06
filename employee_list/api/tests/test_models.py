import pytest

from employees.models import Employee


@pytest.mark.django_db
def test_employee_in_db(employee_first):
    employee_in = Employee.objects.get(first_name = "Jan", last_name = "Nowak")
    assert employee_first == employee_in

@pytest.mark.django_db
def test_change_employee(employee_first):
    employee_first.name = "Aleksander"
    employee_first.save()
    assert employee_first.name == "Aleksander"