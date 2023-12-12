from django.db import models

# Create your models here.
class Employee(models.Model):
    eid= models.IntegerField()
    ename = models.CharField(max_length=32)
    esal = models.IntegerField()
    eloc = models.CharField(max_length=32)

class User(models.Model):
    uname = models.CharField(max_length=32)
    ucity = models.CharField(max_length=32)