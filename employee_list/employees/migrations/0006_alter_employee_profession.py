# Generated by Django 4.0.2 on 2022-02-10 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_profession_alter_employee_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.profession'),
        ),
    ]
