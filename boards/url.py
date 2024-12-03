from django.contrib import admin
from django.urls import path
from .  import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('<int:board_name>/',views.board_topic,name = 'board_topics'),
    path('<int:board_name>/new/',views.new_topic,name = 'new_topic')


]
