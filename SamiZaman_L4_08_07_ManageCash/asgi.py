"""
ASGI config for SamiZaman_L4_08_07_ManageCash project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SamiZaman_L4_08_07_ManageCash.settings')

application = get_asgi_application()
