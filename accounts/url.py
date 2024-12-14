from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import LogoutViewCustom

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='change_pass'),
    path('logout/', LogoutViewCustom.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
