from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    profession = models.CharField(max_length=50)
    avatar = models.ImageField(default='default.jpg')