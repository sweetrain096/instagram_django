from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import UserCustomCreationFrom

# Create your views here.
def signup(request):
    if request.method == "POST":
        user_form = UserCustomCreationFrom(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('posts:list')
            
    else:
        user_form = UserCustomCreationFrom()
    
    context = {"user_form" : user_form}
    return render(request, 'accounts/signup.html', context)
    
def login(request):
    if request.method == 'POST':
        user_form = AuthenticationForm(request, request.POST)
        print(user_form)
        if user_form.is_valid():
            user_form = auth_login(request, user_form.get_user())
        return redirect('posts:list')
    else:
        user_form = AuthenticationForm()
    context = {'user_form' : user_form}
    return render(request, 'accounts/login.html', context)
    
def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    