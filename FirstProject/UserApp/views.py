from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def getindexpage():
    return HttpResponse("Its index page")