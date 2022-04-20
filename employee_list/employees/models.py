from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    profession = models.ForeignKey('employees.Profession', on_delete=models.PROTECT, null=True)
    avatar = models.ImageField(_('Awatar'), help_text=_(' '), default='default.jpg')


class Profession(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name