from django import forms
from .models import UserDetails


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Name"
            }),
            'email': forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your email"
            }),
            'date': forms.DateInput(attrs={
                "class": "form-control",
                "placeholder": "Your date of birth"
            }),
            'password': forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "your password",
            }),
            'confirm password': forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "confirm password",
            }),
        }


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput
        (attrs={
            "name": "email",
            "class": "form-control",
            "type": "email",
            "placeholder": "enter your registered email"
        }))

    password = forms.CharField(
        widget=forms.TextInput(attrs={
            "name": "password",
            "class": "form-control",
            "type": "password",
            "placeholder": "Enter your password"
        }))
