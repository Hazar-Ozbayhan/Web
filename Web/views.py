from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *

from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from django.contrib import messages


def home(request):
    return render(request, 'Pages/Home.html')


def city(request):

    return render(request, 'Pages/City.html')


def comments(request):
    return render(request, 'Pages/Comments.html')

@login_required(login_url='si')
def list(request):
    return render(request, 'Pages/List.html')

@login_required(login_url='si')
def makecomm(request):

    form = CommentForm()
    if request.method == 'POST':
        form =CommentForm(request.POST)
        form.creator=User
        form.givenRate='rates'
        form.place=Place
        if form.is_valid():
            Place.rateCount= Place.rateCount+1
            form.save()
            return redirect('homel')

    return render(request, 'Pages/makecomm.html')


def place(request):
    return render(request, 'Pages/Place.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homel')

        else:
            messages.info(request, 'Email or password is incorrect')

    return render(request, 'Pages/Signin.html')

def logoutUser(request):
    logout(request)
    return redirect('si')

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('si')

    context = {'form':form}
    return render(request, 'Pages/Signup.html', context)

def howToGo(request):
    return render(request,'Pages/howtogo.html')

@login_required(login_url='si')
def homel(request):
    return render(request, 'Pages/Homel.html')

@login_required(login_url='si')
def cityl(request):
    queryset = Place.objects.filter(City.name=='Istanbul')
    print(queryset)
    return render(request, 'Pages/Cityl.html')

@login_required(login_url='si')
def commentsl(request):
    return render(request, 'Pages/Commentsl.html')

@login_required(login_url='si')
def placel(request):
    return render(request, 'Pages/Placel.html')

@login_required(login_url='si')
def howToGol(request):
    return render(request,'Pages/howtogol.html')

@login_required(login_url='si')
def whtg(request):
    return render(request, 'Pages/writehowtogo.html')

@login_required(login_url='si')
def createPlace(request):

    form = PlaceForm()
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        form.creator=User
        if form.is_valid():
            form.save()
            return  redirect('homel')

    context={'form':form}
    return render(request,'Pages/create.html', context)