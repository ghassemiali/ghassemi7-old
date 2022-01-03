from django.urls import path
from blog.views import blog_home, blog_single, test_view

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name='home'),
    path('single/', blog_single, name='blog-single'),
    path('<int:pid>/', test_view, name='test')
]
