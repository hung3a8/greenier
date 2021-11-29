from django.db.models import F
from django.http import JsonResponse
from django.utils.encoding import smart_text
from django.views.generic.list import BaseListView

from product.models import Category, Profile


def _get_user_queryset(term):
    qs = Profile.objects
    if term.endswith(' '):
        qs = qs.filter(user__username=term.strip())
    else:
        qs = qs.filter(user__username__icontains=term)
    return qs


class Select2View(BaseListView):
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.request = request
        self.term = kwargs.get('term', request.GET.get('term', ''))
        self.object_list = self.get_queryset()
        context = self.get_context_data()

        return JsonResponse({
            'results': [
                {
                    'text': smart_text(self.get_name(obj)),
                    'id': obj.pk,
                } for obj in context['object_list']],
            'more': context['page_obj'].has_next(),
        })

    def get_name(self, obj):
        return str(obj)


class UserSelect2View(Select2View):
    def get(self, request, *args, **kwargs):
        if 'multiple_terms[]' not in request.GET:
            return super().get(request, args, kwargs)

        terms = request.GET.getlist('multiple_terms[]')
        qs = Profile.objects.filter(user__username__in=terms).annotate(username=F('user__username')).only('id')

        return JsonResponse({
            'results': [
                {
                    'text': smart_text(self.get_name(obj)),
                    'id': obj.pk,
                } for obj in qs],
        })

    def get_queryset(self):
        return _get_user_queryset(self.term).annotate(username=F('user__username')).only('id')

    def get_name(self, obj):
        return obj.username


class CategorySelect2View(Select2View):
    def get_queryset(self):
        return Category.objects.filter(name__icontains=self.term).annotate(name=F('name')).only('id')
