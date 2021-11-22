from django.conf import settings
from django.views.generic import TemplateView
from product.views.extra import picture_carousel


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(settings, 'HOMEPAGE_PICTURE_CAROUSEL'):
            context['carousel'] = picture_carousel(settings.HOMEPAGE_PICTURE_CAROUSEL, "carousel")
        return context
