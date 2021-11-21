from django.views.generic import DetailView, UpdateView

from product.models.profile import Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'

    def get_object(self):
        return self.request.user.profile


class ProfileUpdateView(UpdateView):
    model = Profile
