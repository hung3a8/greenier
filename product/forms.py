from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from martor.widgets import AdminMartorWidget

from product.models import Product, Profile
from product.widgets import AdminHeavySelect2MultipleWidget, FilemageWidget


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


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'categories', 'price', 'display_image', 'description']

        widgets = {
            'categories': AdminHeavySelect2MultipleWidget(data_view='product_category_select2',
                                                          attrs={'style': 'width: 100%'}),
            'display_image': FilemageWidget(),
            'description': AdminMartorWidget(),
        }


class ProfileEditForm(forms.ModelForm):
    fullname = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Profile
        fields = ['location', 'phone', 'bio']

        widgets = {
            'bio': AdminMartorWidget(),
            'fullname': forms.TextInput(attrs={'style': 'width: 100%;'}),
        }
