from django import forms

class EmployeeForm(forms.ModelForm):
    eid= forms.IntegerField(label="Employee ID")
    ename = forms.CharField(max_length=32, label="Emplloyee Name")
    esal = forms.IntegerField(label="Employee Salary")