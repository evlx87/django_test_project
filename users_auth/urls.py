from django.urls import path

from users_auth.apps import UsersAuthConfig
from users_auth.views import UserLogin, UserLogout, RegisterView, VerifyCodeView

app_name = UsersAuthConfig.name

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_code/', VerifyCodeView.as_view(), name='verify_code')
]
