from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})


def detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.ACTIVE)
    return render(request, 'blog/detail.html', {'post': post})