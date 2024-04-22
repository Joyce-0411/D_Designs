from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from . import models
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    context = {}
    return render(request, 'home.html', context)


def designs(request):
    context = {}
    return render(request, 'designs.html', context)


def contacts(request):
    context = {}
    return render(request, 'contacts.html', context)


def logout(request):
    logout(request)
    return redirect('/')


def login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        user = authenticate(username=uname, password=passwd)
        if user is not None:
            login(request, user)
            return redirect('/wishlist')
    return render(request, 'login.html')


def signin(request):
    form = models.RegisterForm()
    context = {'form': form}
    if request.method == "POST":
        form = models.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            messages.error(request, "User Creation Failed,Try again")
    return render(request, 'signin.html', context)


def help(request):
    context = {}
    return render(request, 'help.html', context)


def trending_designs(request):
    context = {}
    return render(request, 'trending_design.html', context)


def about(request):
    context = {}
    return render(request, 'wishlist.html', context)


def customer_reviews(request):
    context = {}
    return render(request, 'customer_reviews.html', context)
