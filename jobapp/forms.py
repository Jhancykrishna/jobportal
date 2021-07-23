from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser,JobModel,EmployerModel,JobseekerModel,Applications

class RegistrationForm (UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["username","email","Phone","gender","user_type"]

class LoginForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField()


class EmployerForm(forms.ModelForm):
    class Meta:
        model = EmployerModel
        fields = ["company_name", "company_address"]


class JobseekerForm(forms.ModelForm):
    class Meta:
        model = JobseekerModel
        fields = "__all__"


class JobForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = "__all__"

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = "__all__"