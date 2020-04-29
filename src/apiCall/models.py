from django.db import models


# Create your models here.
class apiKeysModel(models.Model):
    key = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.key


class youtubeModel(models.Model):
    video_title = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    publish_datetime = models.DateTimeField(null=False, blank=False)
    thumbnail_url = models.TextField()

    def __str__(self):
        return self.video_title
