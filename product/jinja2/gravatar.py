import hashlib

from django.contrib.auth.models import AbstractUser
from django.utils.http import urlencode

from product.models import Profile
from product.utils.unicode import utf8bytes
from . import registry


@registry.function
def gravatar(email, size=None, default=None):
    if isinstance(email, Profile):
        email = email.user.email
    elif isinstance(email, AbstractUser):
        email = email.email

    gravatar_url = 'https://www.gravatar.com/avatar/' + hashlib.md5(utf8bytes(email.strip().lower())).hexdigest() + '?'
    args = {'d': 'identicon', 's': str(size)}
    if default:
        args['f'] = 'y'
    gravatar_url += urlencode(args)
    return gravatar_url
