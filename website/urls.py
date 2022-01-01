from django.urls import path
from website.views import test_view

urlpatterns = [
    path('http-test/', test_view)
]
