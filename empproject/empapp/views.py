from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from empapp.models import Employee
from empapp.serializers import EmployeeSerializer
# Create your views here.

'''
API URL: http://127.0.0.1:8000/api/create
'''

@api_view(['POST'])
def createemp(request):
    empSerializer = EmployeeSerializer(data=request.data)
    if empSerializer.is_valid():
        empSerializer.save()

    return Response(empSerializer.data)

'''
API URL: http://127.0.0.1:8000/api/
'''
@api_view(['GET'])
def getemp(request):
    empdata= Employee.objects.all()
    empSerializer = EmployeeSerializer(empdata, many=True)
    return Response(empSerializer.data)


'''
API URL: http://127.0.0.1:8000/api/update/<int:id>
'''

@api_view(['POST'])
def updateemp(request,id):
    empdata = Employee.objects.get(id=id)
    empSerializer = EmployeeSerializer(instance=empdata, data=request.data)
    if empSerializer.is_valid():
        empSerializer.save()
    
    return Response(empSerializer.data)


'''
API URL: http://127.0.0.1:8000/api/delete<int:id>
'''
@api_view(['DELETE'])
def deleteemp(request,id):
    empdata = Employee.objects.get(id=id)
    empdata.delete()

    return Response({'msg':'Emp Deleted Sucessfully'})
    