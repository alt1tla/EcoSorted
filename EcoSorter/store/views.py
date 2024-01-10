from django.shortcuts import render, redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

def home(request):
    return render(request,'home.html',{})


def store(request):
    products = Product.objects.all()
    return render(request,'store.html',{'products':products})


def map(request):
    return render(request,'map.html',{})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("Авторизация прошла успешно"))
            return redirect('home')
        else:
            messages.success(request,("При авторизации произошла ошибка"))
            return redirect('login')

    else:    
        return render(request,'login.html',{})



def logout_user(request):
    logout(request)
    messages.success(request,("Деавторизация прошла успешно"))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("Регистрация прошла успешно"))
            return redirect('home')
        else:
            messages.success(request,("При регистрация произошла ошибка"))
            return redirect('register')
    else:
        return render(request,'register.html',{"form":form})
    
def profile(request):
    return render(request,'profile.html',{})

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

def category(request,foo):
    foo = foo.replace("-",'')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, "category.html",{"products":products, "category":category})
    except:
        return redirect ("home")
    return render(request,'product.html',{'product':product})