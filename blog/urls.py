from django.urls import path
from blog.views import blog_home, blog_single, test_view

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name='home'),
    path('single/', blog_single, name='single'),
    path('test/', test_view, name='test')
]
