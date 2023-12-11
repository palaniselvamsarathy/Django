from django.shortcuts import render
import datetime
# Create your views here.

""" def getfirstpage(request):
    date = datetime.datetime.now()
    # date_dict = {
    #     'display_date':date
    # }
    return render(request,'demoapp/first.html',context={'date':date})
 """

def getfirstpage(request):
    message = "Hi"
    date = datetime.datetime.now()
    hour = int(date.strftime('%H'))
    if hour < 12:
        message += " Good Morning"
    else:
         message += " Good Evening"
    name = "Sarathy"
    date_dict = {
        'display_date':date,
        'emp_name':name,
        'age':22,
        'greetings':message
        }
    return render(request,'demoapp/first.html',context = date_dict)
