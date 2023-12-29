
from django.contrib import admin
from django.urls import path
from empapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('create',views.createemp),
    path('',views.getemp),
    path('update/<int:id>',views.updateemp),
    path('delete/<int:id>',views.deleteemp),
]
