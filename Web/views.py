from django.shortcuts import render
from django.http import HttpResponse
from .models import *


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
    return render(request, 'Pages/Signin.html')


def signup(request):
    return render(request, 'Pages/Signup.html')

def howtoGo(request):
    return render(request,'Pages/howtogo.html')