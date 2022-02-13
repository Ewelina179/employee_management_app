from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    profession = models.ForeignKey('employees.Profession', on_delete=models.PROTECT, null=True)
    avatar = models.ImageField(default='default.jpg')


class Profession(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name