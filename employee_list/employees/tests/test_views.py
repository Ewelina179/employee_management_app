import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from employees.models import Employee


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
    assert response.status_code == 200
    assert Employee.objects.filter(id=1).exists() is True

@pytest.mark.django_db
def test_update_employee_view(db, client, employee_first):
    url_kwargs = {'pk': 1}
    url = reverse('update',  kwargs=url_kwargs)
    response = client.post(url, data = {"first_name": "Ewa"})
    assert response.status_code == 200








