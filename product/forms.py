from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)

        self.has_google_auth = self._has_social_auth('GOOGLE_OAUTH2')
        self.has_facebook_auth = self._has_social_auth('FACEBOOK')
        self.has_github_auth = self._has_social_auth('GITHUB_SECURE')

    def _has_social_auth(self, key):
        return (getattr(settings, 'SOCIAL_AUTH_%s_KEY' % key, None) and
                getattr(settings, 'SOCIAL_AUTH_%s_SECRET' % key, None))

    def clean(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user is not None:
            super(CustomAuthenticationForm, self).confirm_login_allowed(user)
        return super(CustomAuthenticationForm, self).clean()

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
