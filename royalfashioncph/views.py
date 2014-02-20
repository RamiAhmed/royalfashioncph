from django.shortcuts import render


# Create your views here.

def home(request):

    return render(request, 'index.html')

def humanstxt(request):

    return render(request, 'humans.txt', content_type="text/plain")

