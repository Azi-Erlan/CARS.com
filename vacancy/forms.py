from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField


class CustomRegisterForm(UserCreationForm):

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "password1",
            "password2",
            "photo",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "gender",
            "city",
            "github",
            "experience_years",
            "stack",
            "about"
        )


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()