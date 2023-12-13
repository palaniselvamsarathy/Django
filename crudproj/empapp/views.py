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

def editpage(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'update.html',{'employee':employee})

def updatepage(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        empdata = EmployeeForm(request.POST, instance=employee)
        if empdata.is_valid():
            try:
                empdata.save()
                return redirect('/read')
            except:
                pass
    return render(request,'update.html')

def deletepage(request,id):
    empdata = Employee.objects.get(id=id)
    empdata.delete()
    return redirect('/read')