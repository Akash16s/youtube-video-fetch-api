from rest_framework import serializers
from apiCall.models import youtubeModel


# Youtube model serializer is for serializing the database model
class youtubeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = youtubeModel
        fields = "__all__"
