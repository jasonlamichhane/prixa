from django.core import validators
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ServerDetails



class ServerDetailsForm(forms.ModelForm):
    class Meta:
        model = ServerDetails
        fields = "__all__"
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']