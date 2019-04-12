from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    
    return render(request, 'posts/list.html', context)


def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save()
            return redirect('posts:detail', post.pk)
    else:
        post_form = PostForm()
    context = {'post_form' : post_form}
    
    return render(request, 'posts/form.html', context)
    
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {'post' : post}
    return render(request, 'posts/detail.html', context)
    
def edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post_form = PostForm(initial=post.__dict__)
    
    context = {'post_form' : post_form}
        
    return render(request, 'posts/form.html', context)
    
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:list')
    else:
        return redirect('posts:detail', post_pk)