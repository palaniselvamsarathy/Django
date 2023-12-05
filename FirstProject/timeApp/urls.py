from django.contrib import admin
from django.urls import path
from timeApp import views

urlpatterns = [
    path('time/',views.tellMeTime)
]