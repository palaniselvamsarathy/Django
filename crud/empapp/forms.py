from django import forms

class EmployeeForm(forms.Form):
    eid = forms.IntegerField(label="ID")
    ename = forms.CharField(max_length=32, label="Name")
    # email = forms.EmailField(label="E-mail")
    esal = forms.FloatField(label="Salary")