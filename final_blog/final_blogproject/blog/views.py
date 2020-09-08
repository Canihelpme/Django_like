from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts': posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.writer = request.user
            post.save()
            return redirect('/' + str(post.id))
    else:
        form = PostForm()
        return render(request, 'create.html', {'form': form})

def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/' + str(post.id))
    else:
        form = PostForm(instance=post)
    return render(request, 'create.html', {'form': form})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('/')

def comments_create(request, post_id):
    post = Post.objects.get(pk=post_id)
    content = request.POST.get('content')
    comment = Comment(post=post, content=content)
    comment.save()
    return redirect('/'+ str(post.id))

def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    
    return redirect('/'+str(post_id))

def comments_update(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('/'+str(post_id))
    
    else:
        return render(request, 'comments_update.html', {'post':post, 'comment':comment})

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        return redirect('home')
    return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        # 해당 데이터의 유저가 있을시
        if user is not None: 
            auth.login(request, user)
            return redirect('home')
        #없을시
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        # POST 요청이 아닐경우 login 페이지 새로고침
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')