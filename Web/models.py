from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name

class kind(models.Model):
    name = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=50,null=True)
    city = models.ForeignKey(City, null=True, on_delete=models.CASCADE)
    where = models.CharField(null=True, max_length=100)
    description = models.CharField(max_length=100,null=True)
    info = models.CharField(null=True, max_length=100)
    kind = models.ForeignKey(kind, null=True, on_delete=models.CASCADE)
    rate = models.IntegerField(null=True,default=0)
    rateCount = models.IntegerField(null=True,default=0)
    Images = ResizedImageField(size=[500, 300], blank=True, null=True)
    canSee = models.BooleanField(null=True, default=False)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Comment(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=25,null=True)
    place = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)
    givenRate = models.IntegerField(null=True)
    comment = models.CharField(max_length=250, null=True)
    commrate = models.IntegerField(null=True, default=0)
    canSee = models.BooleanField(null=True, default=False)

class howToGo(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)
    wayOfTransport = ('BUS','Subway','Seaway','Car')
    description = models.CharField(null=True, max_length=100)

class List(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)