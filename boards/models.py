from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=50,unique=True,null=False)
    desc = models.CharField(max_length=150)

class Topic(models.Model):
    subject = models.CharField(max_length=150)
    board = models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
class Post(models.Model):
    message = models.TextField(max_length=3000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

class User_data(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    creation_date = models.DateTimeField(auto_now_add = True)
    
