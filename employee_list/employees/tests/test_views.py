import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse

from employees.views import EmployeeListView, CreateEmployeeView


def test_employee_list_view(client):
    response = client.get("/")
    content = response.content.decode(response.charset)
    assert response.status_code == 200
    assert "Lista pracowników" in content
    assertTemplateUsed(response, 'employee/list_of_employees.html', 'base.html')

def test_create_employee_view(client, db):
    response = client.post('/create/', data = {"first_name": "Adam", "last_name": "Nowak", "age": "30", "profession": "teacher"})
    assert response.status_code == 302

