from django.urls import path
from .views import *
urlpatterns = [
   path("youtube/", getYoutubeDetails.as_view(), name="baseline Upload"),
]