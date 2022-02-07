from django.shortcuts import render
from .models import Employee

def index(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list_of_employees.html', {'employees': employees})

