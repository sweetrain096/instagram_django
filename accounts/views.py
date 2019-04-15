from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm

from .forms import UserCustomCreationForm, UserCustomChangeForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('posts:list')
            
    else:
        user_form = UserCustomCreationForm()
    
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


def mypage(request, user_name):
    return render(request, 'accounts/mypage.html')
    
def edit(request, user_name):
    if request.method == 'POST':
        user_form = UserCustomChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('posts:list')
    else:
        user_form = UserCustomChangeForm(instance=request.user)

    context = {"user_form" : user_form}
    return render(request, 'accounts/edit.html', context)
    
def password(request, user_name):
    if request.method == 'POST':
        user_form = PasswordChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('posts:list')
    else:
        user_form = PasswordChangeForm(request.user)
    context = { 'user_form' : user_form }
    return render(request, 'accounts/password.html', context)