from django.shortcuts import render
from .models import Employee
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/list_of_employees.html'

class EmployeeView(DetailView):
    model = Employee
    template_name = "employee/employee_detail.html"

class CreateEmployeeView(CreateView):
    model = Employee

    fields = ['first_name', 'last_name', 'age', 'profession', 'avatar']
    success_url ="/"

    template_name = "employee/employee_create_form.html"
    
class UpdateEmployeeView(UpdateView):
    model = Employee
    
    fields = ['first_name', 'last_name', 'age', 'profession', 'avatar']
    success_url ="/"

    template_name = "employee/employee_update_form.html"

class DeleteEmployeeView(DeleteView):
    model = Employee
    success_url ="/"

    template_name = "employee/employee_delete.html"