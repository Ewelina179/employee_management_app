from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee, Profession
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.db.models import Avg
import csv
from django.db.models import Subquery

class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employee/list_of_employees.html'

class EmployeeView(DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = "employee/employee_detail.html"

class CreateEmployeeView(CreateView):
    model = Employee

    form_class = EmployeeForm
    
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
        avg = Employee.objects.all().values('profession').annotate(Avg('age')).order_by('profession_id')
        a = Profession.objects.filter(id__in=Subquery(avg.values('profession'))).all().order_by('id')
        lst=[list(avg), list(a)]
        avg_and_profession_name=zip(*lst)
        context = {
            "avg_and_profession_name": avg_and_profession_name

        }
        return render(request, "employee/report.html", context)


def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="raport.csv"'  
    avg = Employee.objects.all().values('profession').annotate(Avg('age'))  
    writer = csv.writer(response)  
    for element in avg:
        writer.writerow([element['profession'],element['age__avg']])
    return response

class Delete_View(View):
    def post(self, request):
        pass
        return render(request)

class CreateProfessionView(CreateView):
    model = Profession

    fields = ['name']
    success_url ="/"

    template_name = "profession/profession_create.html"
    
class UpdateProfessionView(UpdateView):
    model = Profession
    
    fields = ['name']
    success_url ="/"

    template_name = "profession/profession_update.html"

class DeleteProfessionView(DeleteView):
    model = Employee
    success_url ="/"

    template_name = "employee/employee_delete.html"