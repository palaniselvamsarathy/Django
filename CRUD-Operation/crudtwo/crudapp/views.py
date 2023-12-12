from django.shortcuts import render, redirect
from crudapp.forms import EmployeeForm
from crudapp.models import Employee
# Create your views here.

def createpage(request):
    if request.method == "POST":
        empform = EmployeeForm(request.POST)
        if empform.is_valid():
            try:
                empform.save()
                return redirect('/read/')
            except:
                pass
    else:
        empform = EmployeeForm()
    return render(request,'create.html',{'empform':empform})

def displaypage(request):
    emp_list = Employee.objects.all()
    return render(request,'display.html',{'emp_list':emp_list})

def deletepage(request):
    pass

def updatepage(request):
    pass