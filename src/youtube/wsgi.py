"""
WSGI config for youtube project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from threading import Thread
from apiCall.youtube import youtube
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube.settings')

application = get_wsgi_application()

# this is simple method to fetch the youtube api details by having a thread in start
# this can be done using a celery task running in background
obj = youtube()
# This is the thread call for the function that calls the youtube API at every 10 seconds
Thread(target=obj.saveResults, args=()).start()
