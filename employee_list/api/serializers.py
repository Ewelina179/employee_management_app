from employees.models import Employee, Profession
from rest_framework import serializers
from employee_list import settings

class EmployeeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'age', 'profession', 'avatar']

class ProfessionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profession
        fields = ['id', 'name']