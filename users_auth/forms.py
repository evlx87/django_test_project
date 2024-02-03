from django import forms
from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from users_auth.models import User


class RegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class NewPasswordForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
