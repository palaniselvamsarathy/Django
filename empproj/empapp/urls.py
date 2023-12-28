from django.contrib import admin
from django.urls import path
from empapp import views
urlpatterns = [
    path("",views.getemp),
    path("create", views.createemp),
    path("update/<int:id>",views.updateemp),
    path("delete/<int:id>",views.deleteemp)
]