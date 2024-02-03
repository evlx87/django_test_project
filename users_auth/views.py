from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from users_auth.forms import RegisterForm
from users_auth.models import User


# Create your views here.
class UserLogin(LoginView):
    template_name = 'users_auth/login_form.html'
    success_url = reverse_lazy('catalog:index')


class UserLogout(LogoutView):
    model = User
    success_url = reverse_lazy('catalog:index')


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
