from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from employees.models import Employee, Profession


class EmployeeForm(ModelForm):

    first_name = forms.CharField(
        label=_("Imię"),
        widget=forms.Textarea(attrs={"rows": 1, "cols": 10})
        )
    last_name = forms.CharField(
        label=_("Nazwisko"),
        widget=forms.Textarea(attrs={"rows": 1, "cols": 10})
        )
    age = forms.IntegerField(
        label=_("Wiek")
    )
    profession = forms.ModelChoiceField(
        queryset=Profession.objects.all(),
        label=_('Wybierz zawód z podanych'),
        widget=forms.Select
    )

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'profession', 'age', 'avatar']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)