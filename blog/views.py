from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'section': 'home', 'posts': posts,})

def detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/detail.html', {'section': 'blog_detail', 'post': post,})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'section': 'blog_create', 'form': form,})
