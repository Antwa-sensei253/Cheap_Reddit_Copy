from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Board
from .models import Topic
from django.contrib.auth.models import User
from .models import Topic, Post
def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards': boards})

def about(request):
    return HttpResponse(request,'yes')

def board_topic(request,board_name):
    try:
       board = Board.objects.get(pk=board_name)
    except Board.DoesNotExist:
        raise Http404
    return render(request,'topics.html',{'board': board})

def new_topic(request,board_name):
    try:
       board = Board.objects.get(pk=board_name)
       if request.method == 'POST':
           subject = request.POST['subject']
           message = request.POST['message']
           user = User.objects.first()
           topic = Topic.objects.create(
               subject = subject,
               board = board,
               created_by = user 
           )
           comment  = Post.objects.create(
               message = message,
               topic = topic,
               created_by = user

           ) 
           return redirect('board_topics',board_name=board.pk)
        
    except Board.DoesNotExist:
        raise Http404
    return render(request,'new_topic.html',{'board':board})