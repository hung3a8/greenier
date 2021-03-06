class TitleMixin(object):
    title = '(untitled)'
    content_title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.get_title()
        content_title = self.get_content_title()
        if content_title is not None:
            context['content_title'] = content_title
        return context

    def get_content_title(self):
        return self.content_title

    def get_title(self):
        return self.title
