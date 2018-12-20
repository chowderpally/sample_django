from django.db import models


class ImageModel(models.Model):

    # To hold image
    name = models.CharField(max_length=128, null=False, default='Sample Image')
    images_field = models.BinaryField()

    def __str__(self):
        return self.name


class ImageAttributes(models.Model):

    # Image Attributes
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    img_type = models.CharField(max_length=128, null=True)
    color = models.CharField(max_length=128, null=True)
    variant = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.image
