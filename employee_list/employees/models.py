from django.db import models

class Employee(models.Model):
    PROFESSION = (
        ("web developer", "web developer"),
        ("phtographer", "photographer"),
        ("data analyst", "data analyst"),
        ("teacher", "teacher")
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    profession = models.CharField(max_length=50, choices = PROFESSION)
    avatar = models.ImageField(default='default.jpg')