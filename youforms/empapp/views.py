from django.shortcuts import render
from empapp import forms
# Create your views here.
def empDetails(request):
    form = forms.EmployeeForm()
    empInfo = {'form':form}

    return render(request,'create.html',context = empInfo)