import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from employees.models import Employee
from api.views import CreateEmployeeView, UpdateEmployeeView


def test_employee_list_view(client, db):
    response = client.get("/")
    content = response.content.decode(response.charset)
    assert response.status_code == 200
    assert "Lista pracowników" in content
    assertTemplateUsed(response, 'employee/list_of_employees.html', 'base.html')

@pytest.mark.django_db
def test_employee_view(client, employee_first):
    url_kwargs = {'pk': 1}
    url = reverse('details',  kwargs=url_kwargs)
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "employee/employee_detail.html")

@pytest.mark.django_db
def test_create_employee_view(client, profession_teacher):
    response = client.post('/create/', data = {"first_name": "Adam", "last_name": "Nowak", "age": "30", "profession": profession_teacher})
    employee = EmployeeFactory("ss")
    employee.refresh_from_db()
    assert response.status_code == 200
    assert Employee.objects.filter(first_name="Adam").exists() is True
    assert Employee.objects.count() == 1

@pytest.mark.django_db
def test_update_employee_view(db, client, employee_first, profession_teacher):
    url_kwargs = {'pk': 1}
    url = reverse('update',  kwargs=url_kwargs)
    request = client.post(url, data = {"first_name": "Ewa", "last_name": "Nowak", "age": "33", "profession": profession_teacher})
    #response = UpdateEmployeeView()(request)
    employee_first.refresh_from_db()
    assert employee_first.first_name == "Ewa"
    print(Employee.objects.all())
    #assert response.status_code == 200

@pytest.mark.django_db
def test_delete_employee_view(client, employee_first):
    url_kwargs = {'pk': 1}
    url = reverse('delete',  kwargs=url_kwargs)
    response = client.execute(url)
    assert response.status_code == 200





