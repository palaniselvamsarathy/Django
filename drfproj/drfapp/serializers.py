from rest_framework import serializers
from drfapp.models import Employee
class SerializerEmployee(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields= "__all__"