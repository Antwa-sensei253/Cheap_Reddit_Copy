from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as user_login
from django.contrib.auth.views import LogoutView

from .forms import SignupForm
# Create your views here.
def signup(request):
    form = SignupForm()
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request,user)
            return redirect('home')

    return render(request,'signup.html', {'form':form})


class LogoutViewCustom(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    

def signin(request):
    return render(request,'signin.html')
