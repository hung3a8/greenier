from django import forms
from django.template.loader import get_template

__all__ = ['FilemageWidget']


class FilemageWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None, **kwargs):
        self.template_name = 'widgets/filemage.html'
        template = get_template(self.template_name)
        context = self.get_context(name, value, attrs)
        context['value'] = value.split('\r\n') if value else []
        print(context['value'])
        return template.render(context)

    @property
    def media(self):
        return forms.Media(
            css={
                'all': ('filemage/media.css',),
            },
            js=(),
        )
