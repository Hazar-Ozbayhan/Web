from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField(null=True, max_length=100)
    shortDescribtion = models.CharField(null=True, max_length=100)
    Images = models.ImageField(null=True)

class Place(models.Model):
    name = models.CharField(max_length=50,null=True)
    city = models.ForeignKey(City, null=True, on_delete=models.CASCADE)
    where = models.CharField(null=True, max_length=100)
    descrbtion = models.CharField(max_length=100,null=True)
    info = models.CharField(null=True, max_length=100)
    kind = models.CharField(max_length=30, null=True)
    rate = models.IntegerField(null=True)
    rateCount = models.IntegerField(null=True)
    Images = models.ImageField(null=True)

class Comment(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=25,null=True)
    place = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)
    givenRate = models.IntegerField(null=True)
    comment = models.CharField(max_length=250, null=True)
    commrate = models.IntegerField(null=True)

class howToGo(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)
    wayOfTransport = models.CharField(max_length=10, null=True)
    description = models.CharField(null=True, max_length=100)

class List(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)