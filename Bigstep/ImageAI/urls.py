from django.urls import path
from .views import upload_image, upload_success

urlpatterns = [
    path('', upload_image, name='upload-image'),
    path('upload-success/', upload_success, name='upload-success'),
]
