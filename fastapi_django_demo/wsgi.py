"""
WSGI config for fastapi_django_demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fastapi_django_demo.settings')

application = get_wsgi_application()

app = FastAPI()

from .main import router
app.include_router(router, prefix='/api')
