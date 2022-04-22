import pytest
import uuid

from employees.models import Employee, Profession

@pytest.fixture
def test_password():
    return 'test_pass_1'

@pytest.fixture
def create_user(db, django_user_model, test_password):
   def make_user(**kwargs):
       kwargs['password'] = test_password
       if 'username' not in kwargs:
           kwargs['username'] = str(uuid.uuid4())
       return django_user_model.objects.create_user(**kwargs)
   return make_user

@pytest.fixture
def auto_login_user(db, client, create_user, test_password):
   def make_auto_login(user=None):
       if user is None:
           user = create_user()
       client.login(username=user.username, password=test_password)
       return client, user
   return make_auto_login

@pytest.fixture(scope='session')
def profession_teacher(django_db_setup, django_db_blocker):
     with django_db_blocker.unblock():
        return Profession.objects.create(name="teacher")


@pytest.fixture(scope='session')
def employee_first(django_db_setup, django_db_blocker, profession_teacher):
    with django_db_blocker.unblock():
        return Employee.objects.create(first_name="Jan", last_name="Nowak", age="33", profession=profession_teacher)

@pytest.fixture(scope='session')
def employee_second(django_db_setup, django_db_blocker, profession_teacher):
    with django_db_blocker.unblock():
        return Employee.objects.create(first_name="Jan", last_name="Nowak", age="25", profession=profession_teacher)

@pytest.fixture(scope='session')
def employee_negative(django_db_setup, django_db_blocker, profession_teacher):
    with django_db_blocker.unblock():
        return Employee.objects.create(first_name="Jan", last_name="Nowak", age="nie ma", profession=profession_teacher)
