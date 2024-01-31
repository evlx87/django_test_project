from django.urls import path

from users_auth.apps import UsersAuthConfig
from users_auth.views import UserLogin, UserLogout, RegisterView, UserConfirmEmailView, UserConfirmedView, \
    UserConfirmationFailView

app_name = UsersAuthConfig.name

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm_email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email_confirmed/', UserConfirmedView.as_view(), name='email_confirmed'),
    path('email_confirmation_failed/', UserConfirmationFailView.as_view(), name='email_confirmation_failed'),
]