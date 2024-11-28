from django.contrib import admin
from django.urls import path, re_path

from upswingdata import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('dataretrieval/startTime=<str:startTime>&endTime=<str:endTime>/', views.retrieve, name='retrieve_data')
]

