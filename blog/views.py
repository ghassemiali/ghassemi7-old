from django.shortcuts import render, get_object_or_404
from blog.models import Post

def add_one_in_views(post):
    post.counted_views += 1
    post.save()

def blog_home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    add_one_in_views(post)
    return render(request, 'blog/blog-single.html', context)
    
def test_view(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'posts': post}
    return render(request, 'blog/test.html', context)