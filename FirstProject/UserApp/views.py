from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def getindex(request):
    return render(request,'index.html')
def getabout(request):
    return render(request,'about.html')
def getcontact(request):
    return render(request,'contact.html')