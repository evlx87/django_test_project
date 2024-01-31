from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from users_auth.models import User


class RegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
