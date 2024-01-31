from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, TemplateView

from users_auth.forms import RegisterForm
from users_auth.models import User


# Create your views here.


class UserLogin(LoginView):
    template_name = 'users_auth/login.html'
    success_url = reverse_lazy('catalog:index')


class UserLogout(LogoutView):
    model = User
    success_url = reverse_lazy('catalog:index')


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('users_auth:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse_lazy(
            'users_auth:confirm_email', kwargs={
                'uidb64': uid, 'token': token})

        current_site = '127.0.0.1:8000'

        send_mail(
            subject='Регистрация на платформе',
            message=f"Завершите регистрацию, перейдя по ссылке: http://{current_site}{activation_url}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[
                user.email])
        return redirect('users_auth:email_confirmation_sent')


class UserConfirmEmailView(View):

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(
                user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users_auth:email_confirmed')
        else:
            return redirect('users_auth:email_confirmation_failed')


class UserConfirmedView(TemplateView):
    """ Выводит информацию об успешной регистрации пользователя """
    template_name = 'users_auth/registration_confirmed.html'


class UserConfirmationFailView(View):
    """ Выводит информацию о невозможности зарегистрировать пользователя """
    template_name = 'users_auth/email_confirmation_failed.html'
