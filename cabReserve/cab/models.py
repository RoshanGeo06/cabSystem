from django.db import models
#from django.contrib.auth.models import User
import random

r = print(random.randint(400, 1500))

class TravelInfo(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phoneNo = models.IntegerField()
    boarding = models.CharField(max_length=120)
    destination = models.CharField(max_length=120)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

class VehicleInfo(models.Model):
    Vname = models.CharField(max_length=120)
    Vno = models.CharField(max_length=120)

    def __str__(self):
        return self.Vname + ' --> ' + self.Vno

class Vehicle(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Payment(models.Model):
    Pname = models.CharField(max_length=120)
    cardName = models.CharField(max_length=120)
    cardNumber = models.IntegerField()
    ExpDate = models.DateField()
    cvv = models.IntegerField()

    def __str__(self):
        return self.cardName

