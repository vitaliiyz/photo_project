from django import forms
from account.models import User


class RegistrationForm(forms.ModelForm):
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(attrs={"id": "password_repeat", "required": "required"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {
            "username": forms.TextInput(attrs={"id": "username", "required": "required",}),
            "email": forms.EmailInput(attrs={"id": "email", "required": "required"}),
            "password": forms.PasswordInput(attrs={"id": "password", "required": "required"}),
        }
