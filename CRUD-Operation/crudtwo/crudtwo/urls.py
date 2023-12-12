
from django.contrib import admin
from django.urls import path
from crudapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create",views.createpage),
    path("read",views.displaypage),
    path("delete/",views.deletepage),
    path("update/",views.updatepage)
]
