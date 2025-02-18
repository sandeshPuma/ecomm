from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages # to pop out message
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


# category


def category(request, foo):
    #Replace Hyphens with spaces
    foo = foo.replace('-', ' ')
    # grab the Category
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
        
    except:
        messages.success(request, ("The Category doesnot exists"))
        return redirect('home')


#product 
def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products' : products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (f"{username} have been Logged in"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error"))
            return redirect('login')
          
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You are Logged Out"))
    return redirect('home')
    
    
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            #login user
            user = authenticate(username= username, password= password)
            login(request, user)
            messages.success(request, ("You have Registered SUccessfully!! "))
            return redirect('home')
        
        else:
            messages.success(request, ("Whoops!!! There was a problem"))
            return redirect('register')
    return render(request, 'register.html', {'form': form})


