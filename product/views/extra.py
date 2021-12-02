import os

from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.views.generic import TemplateView


class TitledView(TemplateView):
    """
    A view that renders a template and sets the title to the value
    of the `title` keyword argument.
    """
    title = None
    template_name = 'common-content.html'  # Default, can be changed based on the url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs.get('title', '')
        context['message'] = self.kwargs.get('message', '')
        return context


def generic_message(request, title, message, status=None):
    return render(request, 'common-content.html', {
        'message': message,
        'title': title,
    }, status=status)


def picture_carousel(media_dir, prefix=''):
    if not default_storage.exists(media_dir):
        return []

    files = default_storage.listdir(media_dir)[1]
    return [os.path.join(default_storage.base_url, media_dir, f) for f in files
            if f.startswith(prefix) and f.endswith(settings.SAFE_IMAGE_EXTENSIONS)]
