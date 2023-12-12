from django.shortcuts import render, redirect
from empapp.forms import EmployeeForm
# Create your views here.
def createview(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/read')

            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'create.html',{'form':form})

def readview(request):
    return render(request,'display.html')

def deleteview(request, id):
    pass

def updateview(request):
    pass