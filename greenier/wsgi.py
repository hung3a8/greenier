"""
WSGI config for apicta project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dmoj.settings')

try:
    import MySQLdb  # noqa: F401, imported for side effect
except ImportError:
    import pymysql

    pymysql.install_as_MySQLdb()

from django.core.wsgi import get_wsgi_application  # noqa: E402, django must be imported here
application = get_wsgi_application()
