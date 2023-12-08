from django.shortcuts import render
from userApp.models import User
# Create your views here.

def getuserdata(request):
    user_list = User.objects.all()
    return render(request,'user.html',context={'user_list':user_list})