
from django.contrib import admin
from django.urls import path
from empApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.gethomepage),
    path("add/",views.getempreqpage,name="reg"),
    path("success/",views.getsuccesspage,name="saveemp")
]
