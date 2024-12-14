from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse,Http404
from boards import models

# Create your models here.
def profile(request):
    
    return HttpResponse(request,'yes')