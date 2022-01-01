from django.urls import path
from blog.views import blog_home, blog_single

urlpatterns = [
    path('', blog_home),
    path('single/', blog_single)
]
