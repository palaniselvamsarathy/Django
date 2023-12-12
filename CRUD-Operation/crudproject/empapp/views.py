from django.shortcuts import render, redirect
from empapp.models import Employee
from empapp.forms import EmployeeForm

# Create your views here.
def createview(request):
    if request.method == "POST":
        empform = EmployeeForm(request.POST)
        if empform.is_valid():
            try:
                empform.save()
                return redirect('/read')
            except:
                pass

    else:
        empform = EmployeeForm()
    
    return render(request,'create.html',{'empform':empform})

def displayview(request):
    emp_list = Employee.objects.all()
    return render(request,'display.html',{'emp_list':emp_list})

def deleteview(request,id):
    empdata = Employee.objects.get(id=id)
    empdata.delete()
    return redirect('/read')

def editview(request):
    pass
def updateview(request):
    pass