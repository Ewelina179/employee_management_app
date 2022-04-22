import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from employees.models import Employee
from api.views import CreateEmployeeView, DeleteEmployeeView, UpdateEmployeeView
from api.serializers import EmployeeSerializer, ProfessionSerializer
from rest_framework import serializers

pytestmark = pytest.mark.django_db

def test_employee_list_view(client, db):
    response = client.get("/pl/")
    content = response.content.decode(response.charset)
    assert response.status_code == 200
    assert "Lista pracowników" in content
    assertTemplateUsed(response, 'employee/list_of_employees.html', 'base.html')

def test_employee_view(client, employee_first, auto_login_user):
    url_kwargs = {'pk': 1}
    url = reverse('details',  kwargs=url_kwargs)
    client, user = auto_login_user()
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "employee/employee_detail.html")

#def test_create_employee_view(client, profession_teacher):
#    response = client.post('/create/', data = {"first_name": "Adam", "last_name": "Nowak", "age": "30", "profession": profession_teacher})
#    employee = EmployeeFactory("ss")
#    employee.refresh_from_db()
#    assert response.status_code == 200
#    assert Employee.objects.filter(first_name="Adam").exists() is True
#    assert Employee.objects.count() == 1


def test_update_employee_view(profession_teacher, employee_first, auto_login_user):
    url_kwargs = {'pk': 1}
    url = reverse('update',  kwargs=url_kwargs)
    client, user = auto_login_user()
    response = client.post(url, {"first_name": "Ewa", "last_name": "Nowak", "age": "33", "profession": profession_teacher})
    employee = Employee.objects.get(id=1)
    assert employee.first_name == "Ewa"
    print(Employee.objects.all())
    #assert response.status_code == 200

def test_delete_employee_view(client, employee_first, auto_login_user):
    url_kwargs = {'pk': 1}
    url = reverse('delete',  kwargs=url_kwargs)
    client, user = auto_login_user()
    response = client.post(url)
    assert list(Employee.objects.all()) == list(Employee.objects.none())
    assert response.status_code == 302