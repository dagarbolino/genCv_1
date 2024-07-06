from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login') 
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
    
def custom_logout_view(request):
    logout(request)
    return redirect('pages:home')    