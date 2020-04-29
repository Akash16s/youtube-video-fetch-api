from django.contrib import admin
from .models import apiKeysModel, youtubeModel

# Register your models here.
admin.site.register(apiKeysModel)
admin.site.register(youtubeModel)
