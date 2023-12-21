from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'welcomepage/wp.html')

def maps(request):
    return render(request, 'welcomepage/maps.html')

def store(request):
    return render(request, 'welcomepage/store.html')

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'welcomepage/profile.html')