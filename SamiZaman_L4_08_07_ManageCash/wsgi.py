"""
WSGI config for SamiZaman_L4_08_07_ManageCash project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SamiZaman_L4_08_07_ManageCash.settings')

application = get_wsgi_application()
