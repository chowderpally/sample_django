from django.shortcuts import render
from images.models import ImageModel

# Create your views here.

class UpdateImageView(View):

    def get(self, request, img_id):
        print img_id


        try:
            img = ImageModel.objects.get(image=img)
        except:
            # Show some error



