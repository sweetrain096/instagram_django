from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

from .forms import UserCustomCreationForm, UserCustomChangeForm, ProfileForm
from .models import Profile
from posts.models import Post, Comment
from posts.forms import CommentForm


# Create your views here.
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method == "POST":
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
            return redirect('posts:list')
            
    else:
        user_form = UserCustomCreationForm()
    
    context = {"user_form" : user_form}
    return render(request, 'accounts/signup.html', context)
    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method == 'POST':
        user_form = AuthenticationForm(request, request.POST)
        print(user_form)
        if user_form.is_valid():
            user_form = auth_login(request, user_form.get_user())
        return redirect(request.GET.get('next') or 'posts:list')
    else:
        user_form = AuthenticationForm()
    context = {'user_form' : user_form}
    return render(request, 'accounts/login.html', context)
    
def logout(request):
    auth_logout(request)
    return redirect('posts:list')


def detail(request, user_name):
    User = get_user_model()
    user = get_object_or_404(User, username=user_name)
    posts = user.post_set.order_by('-id')
    comment_form = CommentForm()
    for post in posts:
        post.comments = post.comment_set.all()
        # print(post.comments)
    context = {'user_info' : user, 'posts' : posts, 'comment_form' : comment_form}
    
    return render(request, 'accounts/detail.html', context)
    
def follow(request, user_name):
    User = get_user_model()
    user = get_object_or_404(User, username = user_name)
    
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
        
    return redirect('accounts:detail', user_name)
 
def edit(request, user_name):
    if request.method == 'POST':
        user_form = UserCustomChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, 
                                    request.FILES,
                                    instance=request.user.profile)
        if user_form.is_valid():
            if profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('accounts:detail', user_name)
    else:
        user_form = UserCustomChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {"user_form" : user_form, "profile_form" : profile_form}
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
    
@login_required
def like(request, user_name, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    user = request.user
    # user가 지금 해당 게시글에 좋아요를 한 적이 있는지?
    # if user in post.like_users.all():
    #     post.like_users.remove(user)
    # else:
    #     post.like_users.add(user)
    
    if post.like_users.filter(pk=user.id).exists():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    # return redirect('accounts:mypage', user_name)
    return redirect(request.GET.get('next') or 'posts:list')
    # 