import re

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import get_default_password_validators
from django.db import transaction
from django.utils.translation import gettext, gettext_lazy as _
from registration.backends.default.views import (ActivationView as OldActivationView,
                                                 RegistrationView as OldRegistrationView)
from registration.forms import RegistrationForm
from product.models.profile import Profile

bad_mail_regex = list(map(re.compile, settings.BAD_MAIL_PROVIDER_REGEX))


class CustomRegistrationForm(RegistrationForm):
    username = forms.RegexField(regex=re.compile(r'^\w+$', re.ASCII), max_length=30, label=_('Username'),
                                error_messages={'invalid': _('A username must contain letters, '
                                                             'numbers, or underscores')})
    full_name = forms.CharField(max_length=30, label=_('Full name'), required=False)

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(gettext('The email address "%s" is already taken. Only one registration '
                                                'is allowed per address.') % self.cleaned_data['email'])
        if '@' in self.cleaned_data['email']:
            domain = self.cleaned_data['email'].split('@')[-1].lower()
            if (domain in settings.BAD_MAIL_PROVIDERS or
                    any(regex.match(domain) for regex in bad_mail_regex)):
                raise forms.ValidationError(gettext('Your email provider is not allowed due to history of abuse. '
                                                    'Please use a reputable email provider.'))
        return self.cleaned_data['email']


class RegistrationView(OldRegistrationView):
    form_class = CustomRegistrationForm
    template_name = 'registration/registration_form.html'

    def get_context_data(self, **kwargs):
        kwargs['password_validators'] = get_default_password_validators()
        return super(RegistrationView, self).get_context_data(**kwargs)

    @transaction.atomic
    def register(self, form):
        # Use transaction.atomic to ensure that both user and profile are created in the same transaction.
        user = super(RegistrationView, self).register(form)
        profile = Profile.objects.create(user=user)

        cleaned_data = form.cleaned_data
        user.first_name = cleaned_data['full_name']

        user.save()
        profile.save()

        return user


class ActivationView(OldActivationView):
    pass
