from django.urls import path
from website.views import home_view, about_view, contact_view, elements_view

urlpatterns = [
    path('', home_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('elements/', elements_view),
]
