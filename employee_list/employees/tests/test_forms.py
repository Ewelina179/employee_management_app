import pytest

from employees.forms import EmployeeForm
from employees.models import Employee


def test_employee_form_valid():
    form_data = {
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "age": "30",
        "profession": "teacher",
    }
    form = EmployeeForm(data=form_data)
    assert form.is_valid() is True

def test_employee_form_is_invalid_without_age():
    form_data = {
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "age": None,
        "profession": "teacher"
        }
    form = EmployeeForm(data=form_data)
    assert form.is_valid() is False

def test_employee_form_is_invalid_wrong_profession():
    form_data = {
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "age": "30",
        "profession": "engineer",
        }
    form = EmployeeForm(data=form_data)
    assert form.is_valid() is False