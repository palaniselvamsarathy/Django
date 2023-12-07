from django.shortcuts import render
from userapp.forms import UserForm
from userapp.forms import EmployeeForm
# Create your views here.

def getuserInput(request):
    form = UserForm()
    return render(request,'user.html',context={"form":form})

def gethomepage(request):
    return render(request,'home.html')

def getempinput(request):
    form = EmployeeForm()
    return render(request,'emp.html',{'form':form})