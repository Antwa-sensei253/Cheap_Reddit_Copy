from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
class Board(models.Model):
    name = models.CharField(max_length=50,unique=True,null=False)
    desc = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    def count_posts(self):
        return Post.objects.filter(topic__board=self).count()
    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('created_date').last()


class Topic(models.Model):
    subject = models.CharField(max_length=150)
    board = models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.subject
    def count_posts(self):
        return self.posts.count()
class Post(models.Model):
    message = models.TextField(max_length=3000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)
    updated_dt = models.DateTimeField(null=True)
    def __str__(self): 
        return Truncator(self.message).chars(30) 

class User_data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    creation_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name