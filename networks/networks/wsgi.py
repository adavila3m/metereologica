"""
WSGI config for networks project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir("/home/projects/metereologica/venv_met/lib/python3.11/site-packages")#Agregamos la ruta del entorno virtual
sys.path.append("/home/projects/metereologica/networks")
sys.path.append("/home/projects/metereologica/networks/networks")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'networks.settings')

application = get_wsgi_application()
