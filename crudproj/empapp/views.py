from django.shortcuts import render, redirect
from empapp.forms import EmployeeForm
from empapp.models import Employee
# Create your views here.
def createpage(request):
    if request.method == "POST":
        empform = EmployeeForm(request.POST)
        if empform.is_valid():
            try:
                empform.save()
                return redirect("/read")
            except:
                pass

    else:
        empform = EmployeeForm()
    return render(request,'create.html',{'empform':empform})

def displaypage(request):
    emp_list = Employee.objects.all()
    return render(request,'display.html',{'emp_list':emp_list})

def editpage(request):
    pass

def deletepage(request):
    pass