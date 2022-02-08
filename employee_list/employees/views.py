from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Employee
from .forms import GetReportForm
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

class ReportView(View):
    def get(self, request):
        form = GetReportForm()
        context = {
            'form':form,
        }
        return render(request, "employee/report.html", context)

    def post(self, request):
        form = GetReportForm(request.POST)
        if form.is_valid():
            obj = form.cleaned_data
            x = obj['profession']
            counter = Employee.objects.filter(profession=x).all()
            age = [x.age for x in counter]
            average = (sum(age)/len(age))
            print(average)
            return HttpResponse("jest dobrze!")
        else:
            context = {
            'form':form,
        }
        return render(request, "employee/report.html", context)

class DeleteEmployeeView(View):
    def post(self, request):
        pass
        return render(request)