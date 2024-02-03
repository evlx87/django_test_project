import random
import string

from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import CreateView, FormView

from users_auth.forms import RegisterForm, NewPasswordForm
from users_auth.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('users_auth:verify_code')
    template_name = 'users_auth/registration_form.html'

    def form_valid(self, form):
        user = form.save()

        send_mail(
            subject='Регистрация на платформе',
            message=f"Код подтверждения: {user.verify_code}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email])
        return super().form_valid(form)


class VerifyCodeView(View):
    model = User
    template_name = 'users_auth/verifycode_form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(verify_code=request.POST.get('verify_code')).first()
        if user:
            user.is_verified = True
            user.save()
            return redirect('users_auth:login')

        return redirect('users_auth:verify_code')


class PasswordResetView(FormView):
    template_name = 'users_auth/password_reset_form.html'
    form_class = NewPasswordForm
    success_url = reverse_lazy('user_auth:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.get(email=email)

        pass_symbols = ''.join(random.choice(string.ascii_letters + string.digits + '!@#$%&'))
        password = get_random_string(12, pass_symbols)

        user.set_password(password)
        user.save()

        send_mail(
            subject='Пароль восстановлен',
            message=f'Ваш новый пароль: {password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)
