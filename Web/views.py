from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login , logout

from .forms import CreateUserForm
from django.contrib import messages


def home(request):
    return render(request, 'Pages/Home.html')


def city(request):
    return render(request, 'Pages/City.html')


def comments(request):
    return render(request, 'Pages/Comments.html')


def list(request):
    return render(request, 'Pages/List.html')


def makecomm(request):
    return render(request, 'Pages/makecomm.html')


def place(request):
    return render(request, 'Pages/Place.html')


def signin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('psw')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('')

        else:
            messages.info(request, 'Email or password is incorrect')

    return render(request, 'Pages/Signin.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'Pages/Signup.html', context)

def howToGo(request):
    return render(request,'Pages/howtogo.html')

def homel(request):
    return render(request, 'Pages/Homel.html')

def cityl(request):
    return render(request, 'Pages/Cityl.html')

def commentsl(request):
    return render(request, 'Pages/Commentsl.html')

def placel(request):
    return render(request, 'Pages/Placel.html')

def howToGol(request):
    return render(request,'Pages/howtogol.html')
