from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from curriculum.models import Info

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
    return redirect('pages:dashboard')    



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pages:home')  
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def user_info_view(request):
    if not request.user.is_authenticated:
        return redirect('users:login') 
    user_data = Info.objects.filter(user=request.user)  
    return render(request, 'users/user_info.html', {'data': user_data})