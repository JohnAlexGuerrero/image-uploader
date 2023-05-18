from django.db import models

from PIL import Image
from slugify import slugify

class Gallery(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Gallery")
        verbose_name_plural = ("Galleries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ''

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000/' + self.image.url
        
        return ''
