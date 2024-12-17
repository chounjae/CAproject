from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api/beautify/', views.beautify_text, name='beautify_text'),
    
]

#뷰 파일에서 api 호출 