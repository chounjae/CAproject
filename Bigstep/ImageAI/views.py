from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageModel

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload-success')  # 성공 후 리다이렉트
    else:
        form = ImageUploadForm()
    return render(request, 'imageai.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')  # 업로드 성공 페이지
