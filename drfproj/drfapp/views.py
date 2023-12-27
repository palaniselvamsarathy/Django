from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drfapp.models import Employee
from drfapp.serializers import SerializerEmployee
# Create your views here.

@api_view(['GET'])
def home(request):
    emp_data = Employee.objects.all()
    emp_serializer = SerializerEmployee(emp_data, many=True)
    return Response({'status':400,'message':'Success','avail':True,'payload':emp_serializer.data})

@api_view(['GET'])
def emp_data(request):
    emp_data = Employee.objects.all()
    emp_serializer = SerializerEmployee(emp_data, many=True)
    return Response({'messages':emp_serializer.data})