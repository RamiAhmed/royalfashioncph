from django.shortcuts import render


# Create your views here.

def home(request):

    return render(request, 'index.html')
  
def springcollection(request):
    
    return render(request, 'collection.html')

def omos(request):
    
    return render(request, 'omos.html')

def humanstxt(request):

    return render(request, 'humans.txt', content_type="text/plain")

