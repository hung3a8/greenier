from django.views.generic import DetailView

from judge.models import Profile


class UserProfileView(DetailView):
    model = Profile
    template_name = 'user/user-detail.html'

    def get_object(self):
        return self.request.user.profile
