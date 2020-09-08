from .models import Post
from django.shortcuts import render, redirect, get_object_or_404
from faker import Faker
from django.utils import timezone

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})

def create10(request):
    ifake = Faker()
    for i in range(10):
        post = Post()
        post.title = ifake.name()
        post.body = ifake.sentence()
        post.pub_date = timezone.datetime.now()
        post.save()
    return redirect('/')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})