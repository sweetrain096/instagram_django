from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Post, Comment
from .forms import PostForm, ImageForm, CommentForm

# Create your views here.
@login_required
def list(request):
    # 내가 팔로우 한 글만 보기
    # posts = Post.objects.filter(user__in=request.user.followings.all()).order_by('-id')
    # post에 들어오는 내용을 내가 쓴 글까지 확인하기
    
    posts = Post.objects.filter(
                        Q(user__in=request.user.followings.values('id'))
                        | Q(user=request.user.id)
                        ).order_by('-pk')
    comment_form = CommentForm()
    for post in posts:
        post.comments = post.comment_set.all()[:2]
        # print(post.comments)
    context = {'posts' : posts, 'comment_form' : comment_form}
    
    return render(request, 'posts/list.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            files = request.FILES.getlist('file')
            for file in files:
                request.FILES['file'] = file
                image_form = ImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
        image_form = ImageForm()
    context = {'post_form' : post_form, 'image_form' : image_form}
    
    return render(request, 'posts/form.html', context)
    
def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    posts = Post.objects.order_by('-id')
    context = {'post' : post, 'posts' : posts}
    return render(request, 'posts/detail.html', context)
    
@login_required
def edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post.content = post_form.cleaned_data.get('content')
            post.save()
            
            return redirect('posts:list')
    else:
        post_form = PostForm(initial=post.__dict__)
    
    context = {'post_form' : post_form}
    return render(request, 'posts/form.html', context)
   
@login_required 
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:list')
    else:
        return redirect('posts:detail', post_pk)
        

    
def create_comment(request, post_pk):
    print(post_pk)
    post = Post.objects.get(pk = post_pk)
    # comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
    return redirect(request.GET.get('next') or 'posts:list')
    # return redirect('posts:list')