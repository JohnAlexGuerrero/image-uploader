from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from uploader.forms import UploaderForm
from uploader.models import Gallery

class GalleryView(TemplateView):
    template_name = "gallery.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gallery"] = Gallery.objects.all()
        print(context)
        return context
    
class ImageDetailView(TemplateView):
    template_name = "detail.html"


class UploaderView(TemplateView):
    template_name = "uploader.html"
    form_class = UploaderForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('gallery.html')
        else:
            return self.render_to_response(self.get_context_data(form=form))
    

