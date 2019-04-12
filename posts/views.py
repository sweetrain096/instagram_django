from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, ImageForm

# Create your views here.
def list(request):
    posts = Post.objects.order_by('-id')
    context = {'posts' : posts}
    
    return render(request, 'posts/list.html', context)


def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save()
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
    
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:list')
    else:
        return redirect('posts:detail', post_pk)