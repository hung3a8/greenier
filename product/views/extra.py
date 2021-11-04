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
        return context
