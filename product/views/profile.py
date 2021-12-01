from django.contrib.auth.views import redirect_to_login
from django.http import Http404
from django.views.generic import DetailView, UpdateView

from product.models import Profile
from product.models.product import Product
from product.views import generic_message


class UserMixin(object):
    model = Profile
    slug_field = 'user__username'
    slug_url_kwarg = 'user'
    context_object_name = 'user'

    def render_to_response(self, context, **response_kwargs):
        return super(UserMixin, self).render_to_response(context, **response_kwargs)


class ProfileDetailView(UserMixin, DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(seller=self.object)
        return context

    def get_object(self, queryset=None):
        if self.kwargs.get(self.slug_url_kwarg, None) is None:
            return self.request.user.profile
        return super(ProfileDetailView, self).get_object(queryset)

    def dispatch(self, request, *args, **kwargs):
        if self.kwargs.get(self.slug_url_kwarg, None) is None:
            if not self.request.user.is_authenticated:
                return redirect_to_login(self.request.get_full_path())
        try:
            return super(ProfileDetailView, self).dispatch(request, *args, **kwargs)
        except Http404:
            return generic_message(request, title='No such user', message='No username "%s".' %
                                   self.kwargs.get(self.slug_url_kwarg, None))


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profile/profile_update.html'
