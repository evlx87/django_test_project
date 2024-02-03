from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users_auth.apps import UsersAuthConfig
from users_auth.views import RegisterView, VerifyCodeView, PasswordResetView, reset_password

app_name = UsersAuthConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users_auth/login_form.html'), name='login'),
    path('', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_code/', VerifyCodeView.as_view(), name='verify_code'),
    # path('pass_reset/', PasswordResetView.as_view(), name='pass_reset'),
    path('pass_reset/', reset_password, name='pass_reset'),
]
