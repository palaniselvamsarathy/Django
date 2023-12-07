from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(verbose_name="Employee ID")
    ename = models.CharField(max_length=32,verbose_name="Employee Name")
    esal = models.FloatField(verbose_name="Employee Salary")
