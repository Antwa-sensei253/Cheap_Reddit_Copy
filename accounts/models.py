from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from boards.models import User_data
# Create your models here.

@login_required
def profile(request):
    user = request.user 
    user_data = get_object_or_404(User_data, user=user)  # Fetch User_data safely
    return render(request, 'profile.html', {'user': user, 'user_data': user_data})
