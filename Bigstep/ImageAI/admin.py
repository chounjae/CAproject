from django.contrib import admin
from .models import ImageModel

class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

admin.site.register(ImageModel, ImageModelAdmin)
