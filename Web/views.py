from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .models import Place
from .forms import CreateUserForm
from django.contrib import messages
from django.urls import reverse


def home(request):
    return render(request, 'Pages/Home.html')

class Istanbul(ListView):
    model = Place



    template_name = 'Pages/City.html'



class PPlace(DetailView):
    model = Place
    peke = Place

    template_name = 'Pages/Place.html'





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
            Place.rate=Place.rate * Place.rateCount
            Place.rate=Place.rate+form.givenRate
            Place.rateCount= Place.rateCount+1
            Place.rate/=Place.rateCount
            form.save()
            return redirect('homel')

    return render(request, 'Pages/makecomm.html')


def place(request):
    form = ListForm()

    if request.method == 'POST':
        form=ListForm(request.POST)
        form.user=User
        if form.is_valid():
            form.save()

    return render(request, 'Pages/Place.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

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

class Izmir(ListView):
    model = Place



    template_name = 'Pages/Izmir.html'

class Ankara(ListView):
    model = Place



    template_name = 'Pages/Ankara.html'





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