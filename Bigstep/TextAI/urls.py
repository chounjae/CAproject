from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # 기본 화면
    path('api/beautify/', views.beautify_text, name='beautify_text'),  # 여기가 API 엔드포인트
    
]
