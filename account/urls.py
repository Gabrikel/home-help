from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views

# https://docs.djangoproject.com/en/3.1/topics/auth/default/
# https://ccbv.co.uk/projects/Django/3.0/django.contrib.auth.views/PasswordResetConfirmView/

app_name = 'account'

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('register/', views.account_register, name='register'),
]