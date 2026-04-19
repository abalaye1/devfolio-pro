"""
WSGI config for devfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Default to production for WSGI
os.environ.setdefault('ENVIRONMENT', 'production')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devfolio.settings.production')

application = get_wsgi_application()
