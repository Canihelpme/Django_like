from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects #모든 블로그 글 대상
    posts_list=Post.objects.all() #모든 objects list화
    paginator = Paginator(posts_list, 3) #블로그 객체 세 개를 한 페이지로 자르자.
    page = request.GET.get('page') #request된 페이지가 뭔지를 알아냄.
    posts_num = paginator.get_page(page) #request된 페이지를 얻어온 뒤 return.

    return render(request, 'home.html', {'blogs':posts, 'posts_num': posts_num})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def new(request):
    return render(request, 'post/new.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/blog/' + str(post.id))

def delete(request, post_id):
    post_num = get_object_or_404(Post, pk=post_id)
    post_num.delete()
    return redirect('/')
    
#10개정도 random으로 만들기
"""def create10(request):
    myfake = Faker()
    for i in range(10):
        post = Post()
        post.title = myfake.name()
        post.body = myfake.sentence()
        post.pub_date = timezone.datetime.now()
        post.save()
    return redirect('/')
"""
