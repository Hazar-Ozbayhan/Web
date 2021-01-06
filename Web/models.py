from django.db import models

# Create your models here.
"""class City(models.Model):
    name = models.CharField

class Place(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City)
    where = models.CharField
    descrbtion = models.CharField(max_length=100)
    info = models.CharField
    kind = models.CharField(max_length=30)
    rate = models.IntegerField
    Images = models.ImageField

class User(models.Model):
    name = models.CharField
    email = models.EmailField
    password= models.CharField

class Comment(models.Model):
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=25)
    place = models.ForeignKey(Place)
    givenRate = models.IntegerField
    comment = models.CharField(max_length=250)
    commrate = models.IntegerField

class howToGo(models.Model):
    creator = models.ForeignKey(User)
    place = models.ForeignKey(Place)
    wayOfTransport = models.CharField(max_length=10)
    description = models.CharField

class List(models.Model):
    user = models.ForeignKey(User)
    place = models.ForeignKey(Place)"""