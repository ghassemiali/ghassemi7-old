from django import template
from blog.models import Post

register = template.Library()

@register .simple_tag
def hello():
    return ("hello")

@register .simple_tag(name='dardo')
def function(input_number = 3):
    return input_number * 2

@register .simple_tag(name='totalposts')
def function_2():
    posts = Post.objects.filter(status=1).count()
    return posts

@register .simple_tag(name='allposts')
def function_3():
    posts = Post.objects.filter(status=1)
    return posts

