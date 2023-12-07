from django import forms
from userapp.models import Employee
class UserForm(forms.Form):
    uid = forms.IntegerField(label="User ID")
    uname = forms.CharField(max_length=50,label="User Name")
    uloc = forms.CharField(max_length=32,label="Location")
    uemail = forms.CharField(max_length=100,label="Email")

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = "__all__"
        fields= ['eid','ename','esal']