from django.contrib import admin
from django.urls import path, include
from . import views

app_name ='UseapiConfig'
urlpatterns = [
    path('', views.start),
]