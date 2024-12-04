from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Board
from django.contrib.auth.models import User
from .models import Topic, Post
from .forms import NewTopicFrom

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
def new_topic(request, board_name):
    try:
        board = Board.objects.get(pk=board_name)
        form = NewTopicFrom()
        user = User.objects.first()
        if request.method == "POST":
            form = NewTopicFrom(request.POST)
            if form.is_valid():
                topic = form.save(commit=False)
                topic.board = board
                topic.created_by = user
                topic.save()

                post = Post.objects.create(
                    message=form.cleaned_data.get('message'),
                    created_by=user,
                    topic=topic
                )
                return redirect('board_topics', board_name=board.pk)
        else:
            form = NewTopicFrom()
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'new_topic.html', {'board': board, 'form': form})
