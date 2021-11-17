from django.views.generic import DetailView
from django.views.generic.edit import UpdateView

from product.models.profile import Profile


class UserProfileView(DetailView):
    model = Profile
    template_name = 'user/user-detail.html'

    def get_object(self):
        return self.request.user.profile


class ProfileEditView(UpdateView):
    model = Profile
    fields = [
        'avatar',
        'first_name',
        'last_name',
        'phone',
        'email'
        'bio'
    ]
