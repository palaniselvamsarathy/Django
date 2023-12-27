from django.shortcuts import render


# Create your views here.
def cookies_count(request):
    count = request.COOKIES.get('count',0)
    totalCount = int(count)+1

    response = render(request, 'cookiescount.html',{'count':totalCount})
    response.set_cookie('count',totalCount)
    return response