from django.shortcuts import render
from blog.models import Post

def blog_home(request):
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    return render(request, 'blog/blog-single.html')
    
def test_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/test.html', context)