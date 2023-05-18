from django.urls import path

from uploader.views import UploaderView
from uploader.views import GalleryView
from uploader.views import ImageDetailView

urlpatterns = [
    path('list/', GalleryView.as_view(), name='gallery'),
    path('<slug:slug_image>/', ImageDetailView.as_view(), name='image_details'),
    path('', UploaderView.as_view(), name='images'),
]
