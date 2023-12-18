from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'welcomepage/wp.html')

def maps(request):
    return render(request, 'welcomepage/maps.html')
