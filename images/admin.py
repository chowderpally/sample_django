from django.contrib import admin
from images.models import ImageModel, ImageAttributes

admin.site.register(ImageModel)
admin.site.register(ImageAttributes)
