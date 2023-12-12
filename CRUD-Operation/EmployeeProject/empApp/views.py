from django.shortcuts import render
from empApp.forms import EmployeeForm,UserForm
from empApp.models import Employee,User

# Create your views here.
def gethomepage(request):
    return render(request,'home.html')

def getempreqpage(request):
    empform = EmployeeForm()
    return render(request,'emp.html',{'empform':empform})

# def getsuccesspage(request):
#     if request.method == 'POST':
#         eid = request.POST['eid']
#         ename = request.POST.get('ename')
#         esal = request.POST['esal']
#         eloc = request.POST['eloc']


#         empdata = Employee(eid=eid,ename=ename, esal=esal,eloc=eloc)
#         empdata.save()
#     return render(request,'success.html')

def getsuccesspage(request):
    if request.method=="POST":
        empdata = EmployeeForm(request.POST)
        if empdata.is_valid():
            empdata.save()
    return render(request,'success.html')

def getuserreqpage(request):
    userform = UserForm()
    return render(request,'usermain.html',{'userform':userform})

def getuserpage(request):
    if request.method == "POST":
        userdata = UserForm(request.POST)
        if userdata.is_valid():
            userdata.save()
    return render(request,'user.html')