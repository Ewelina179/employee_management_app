from random import choice
from django.forms import ModelForm, SelectMultiple
from django import forms
from .models import Employee, Profession

class EmployeeForm(ModelForm):

    profession = forms.ModelChoiceField(
                       widget = forms.Select,
                       queryset = Profession.objects.all()
               )

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'age', 'profession', 'avatar']
    