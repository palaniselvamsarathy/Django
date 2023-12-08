from django.shortcuts import render
from dbapp.models import Employee
# Create your views here.

def getusercontent(request):
    user_list = Employee.objects.all()
    user_data = {'user_list':'user_list'}
    return render(request,'user.html',context=user_data)