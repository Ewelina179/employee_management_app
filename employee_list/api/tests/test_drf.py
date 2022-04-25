import pytest

from rest_framework import routers
from django.urls import reverse
import json 

pytestmark = pytest.mark.django_db

def test_get_profession_should_return_empty_list_when_db_empty(client):
    response = client.get('/en/professions/')
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_professions_exist_should_succeed(client, profession_teacher):
    response = client.get('/en/professions/1/')
    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content.get("name") == "teacher"