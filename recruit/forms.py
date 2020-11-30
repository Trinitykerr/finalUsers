from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Contact


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required. Add a vaild email address')

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2", "type")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'age', 'message']
