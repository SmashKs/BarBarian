"""
WSGI config for BarBarian project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

from log.logger import Logger

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BarBarian.settings')

application = get_wsgi_application()

Logger.basic_setting()
