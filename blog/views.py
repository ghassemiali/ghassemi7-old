from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request):
    return render(request, 'blog/blog-single.html')
    
def test_view(request, postnumber):
    post = get_object_or_404(Post, pk=postnumber)
    context = {'posts': post}
    return render(request, 'blog/test.html', context)