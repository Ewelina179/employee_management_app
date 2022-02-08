from django.forms import ModelForm
from django import forms
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'age', 'profession', 'avatar']

FILE_FORMAT = (
    ("json", "json"),
    ("csv", "csv")
)

unique_profession_of_employees = Employee.objects.distinct("profession").all()
professions = unique_profession_of_employees.values("profession")

class GetReportForm(forms.Form):
    # dwa choices - z modelu profession, z wyborów na sztywno format pliku
    profession = forms.ModelChoiceField(queryset=professions)
    file_format = forms.ChoiceField(choices = FILE_FORMAT)


