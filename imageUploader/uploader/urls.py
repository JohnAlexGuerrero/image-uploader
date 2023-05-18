from django.urls import path

from uploader.views import UploaderView

urlpatterns = [
    path('', UploaderView.as_view(), name='images'),
]
