from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image
from django.utils.text import slugify

class Gallery(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Gallery")
        verbose_name_plural = ("Galleries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.slug is None:
            self.slug = slugify(self.name)
            self.save()
            
        return f'http://127.0.0.1:8000/images/{self.slug}'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        
        return ''

@receiver(post_save, sender=Gallery)
def save_slug_comic(sender, instance, created, **kwargs):
    image = Gallery.objects.get(name=instance)
    
    if created:
        image.slug = slugify(image.name)
        image.save()