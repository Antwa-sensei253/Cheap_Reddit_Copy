from datetime import timezone
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Board
from django.contrib.auth.models import User
from .models import Topic, Post
from .forms import NewTopicFrom
from .forms import newReplyForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.views.generic import UpdateView
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def about(request):
    return HttpResponse('About Page')

def board_topic(request, board_name):
    board = get_object_or_404(Board, name=board_name)
    topics = board.topics.order_by('-created_date').annotate(replies=Count('posts')-1)
    return render(request, 'topics.html', {'board': board,'topics': topics})

@login_required
def new_topic(request, board_name):
    board = get_object_or_404(Board, name=board_name)
    form = NewTopicFrom()
    if request.method == "POST":
        form = NewTopicFrom(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                created_by=request.user,
                topic=topic
            )
            return redirect('board_topics', board_name=board.name)
    return render(request, 'new_topic.html', {'board': board, 'form': form})

def topic_posts(request, board_name, topic_name):
    board = get_object_or_404(Board, name=board_name)
    topic = get_object_or_404(Topic, board=board, subject=topic_name)
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})

@login_required
def post_reply(request, board_name, topic_name):
    board = get_object_or_404(Board, name=board_name)
    topic = get_object_or_404(Topic, board=board, subject=topic_name)
    if request.method == "POST":
        form = newReplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', board_name=board.name, topic_name=topic.subject)
    else:
        form = newReplyForm()
    return render(request, 'post_reply.html', {'topic': topic, 'form':form})

@login_required
def post_reply(request, board_name, topic_name):
    board = get_object_or_404(Board, name=board_name)
    topic = get_object_or_404(Topic, board=board, subject=topic_name)
    if request.method == "POST":
        form = newReplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', board_name=board.name, topic_name=topic.subject)
    else:
        form = newReplyForm()
    return render(request, 'post_reply.html', {'topic': topic, 'form':form})

class PostUpdateView(UpdateView):
    model = Post
    fields = ('message',)
    template_name = 'edit_post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_dt = timezone.now()
        post.save()
        return redirect('topic_posts', board_name=post.topic.board.name, topic_name=post.topic.subject)