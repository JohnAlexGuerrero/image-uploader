from django import forms

from uploader.models import Gallery

class UploaderForm(forms.ModelForm):
    image = forms.FileField(max_length=200, required=True)
    class Meta:
        model = Gallery
        fields = ("image",)
