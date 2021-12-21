from django import forms
from .models import UserDetails


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__"
        # widgets = {
        #     "name": forms.TextInput(attrs={
        #         "class": "form-control",
        #         "placeholder": "Your Name"
        #     }),
        #     'email': forms.EmailInput(attrs={
        #         "class": "form-control",
        #         "placeholder": "Your email"
        #     }),

        #     'date': forms.DateInput(attrs={
        #         "class": "form-control",
        #         "placeholder": "Your date of birth"
        #     }),

        #     'image': forms.Textarea(attrs={
        #         "class": "form-control",
        #         "placeholder": "write your message",
        #     }),
        #     'password': forms.PasswordInput(attrs={
        #         "class": "form-control",
        #         "placeholder": "your password",
        #     }),
        #     'confirm password': forms.PasswordInput(attrs={
        #         "class": "form-control",
        #         "placeholder": "confirm password",
        #     }),
        # }
