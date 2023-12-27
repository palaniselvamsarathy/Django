from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drfapp.models import Employee
from drfapp.serializers import EmployeeSerializer
# Create your views here.

'''
API URL: http://127.0.0.1:8000/
Method: GET
Required Fields: None
ACCESS type: Public
'''

@api_view(['GET'])
def home(request):
    emp_data = Employee.objects.all()
    emp_serializer = EmployeeSerializer(emp_data, many= True)
    return Response({'status':200,'message':'Home Page Response','avail':True,'payload':emp_serializer.data})

@api_view(['GET'])
def emp_data(request):
    emp_data = Employee.objects.all()
    emp_serializer = EmployeeSerializer(emp_data, many= True)
    return Response({'employees':emp_serializer.data})