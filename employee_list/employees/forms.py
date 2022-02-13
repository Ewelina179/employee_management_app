from django import forms
from django.forms import ModelForm

from .models import Employee, Profession


class EmployeeForm(ModelForm):

    first_name = forms.CharField(
        label="Imię",
        widget=forms.Textarea(attrs={"rows": 1, "cols": 10})
        )
    last_name = forms.CharField(
        label="Nazwisko",
        widget=forms.Textarea(attrs={"rows": 1, "cols": 10})
        )
    age = forms.IntegerField(
        label="Wiek"
    )
    profession = forms.ModelChoiceField(
        queryset=Profession.objects.all(),
        label='Wybierz zawód z podanych',
        widget=forms.Select
    )

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'profession', 'age', 'avatar']
