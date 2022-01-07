from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime

def add_one_in_views(post):
    post.counted_views += 1
    post.save()

def blog_home(request):
    x = datetime.timedelta(hours=3, minutes=30)
    now = datetime.datetime.now().astimezone(datetime.timezone(x))
    posts = Post.objects.filter(status=1, published_date__lte=now)    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    x = datetime.timedelta(hours=3, minutes=30)
    now = datetime.datetime.now().astimezone(datetime.timezone(x))
    posts = Post.objects.filter(status=1, published_date__lte=now)     
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post}
    add_one_in_views(post)
    return render(request, 'blog/blog-single.html', context)
    
def test_view(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'posts': post}
    return render(request, 'blog/test.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1, category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


    