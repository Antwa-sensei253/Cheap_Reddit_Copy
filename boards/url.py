from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<str:board_name>/', views.board_topic, name='board_topics'),
    path('<str:board_name>/new/', views.new_topic, name='new_topic'),
    path('<str:board_name>/topics/<str:topic_name>/', views.topic_posts, name='topic_posts'),
    path('<str:board_name>/topics/<str:topic_name>/reply', views.post_reply, name='post_reply'),
    path('<str:board_name>/topics/<str:topic_name>/posts/<int:post_id>/edit', views.PostUpdateView.as_view(), name='edit_post'),

]