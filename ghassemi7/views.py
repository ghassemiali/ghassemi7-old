from django.http import HttpResponse

def test_view(request):
    return HttpResponse('<h1>test page</h1>')