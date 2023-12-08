from django.shortcuts import render
from empApp.forms import EmployeeForm
# Create your views here.
def gethomepage(request):
    return render(request,'home.html')

def getemppage(request):
    pass

def getsuccesspage(request):
    pass