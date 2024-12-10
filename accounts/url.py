from django.contrib import admin
from django.urls import path
from .  import views
from django.contrib.auth import views as auth_views
from .views import LogoutViewCustom
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name='login'),
    path('logout/', LogoutViewCustom.as_view(), name='logout'),
    

]
