from django import forms
from empApp.models import Employee
# class EmployeeForm(forms.Form):
#     eid = forms.IntegerField(label="Employee ID")
#     ename = forms.CharField(label="Employee Name")
#     esal = forms.IntegerField(label="Employee Salary")
#     eloc = forms.CharField(label="Employee Location")

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['eid','ename','eloc','esal']