from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def getindexpage(request):
    msg = '<h1>Its index page</h1>'
    return HttpResponse(msg)