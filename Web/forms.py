from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class   Meta:
        model = User
        fields= ['email','username','password1','password2']

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name','city','where','description','info','kind','Images','creator']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields= ['place','givenRate','comment']
