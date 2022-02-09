import pytest

from employees.models import Employee
from employees.forms import EmployeeForm

@pytest.mark.django_db
def test_employee_form_valid():
    form_data = {
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "age": "30",
        "profession": "teacher",
    }
    form = EmployeeForm(data=form_data)
    assert form.is_valid() is True

