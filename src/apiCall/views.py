from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from apiCall.models import youtubeModel
from apiCall.serializers import youtubeModelSerializer
from django_filters.rest_framework import DjangoFilterBackend


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# Create your views here.
class getYoutubeDetails(generics.ListAPIView):
    queryset = youtubeModel.objects.order_by("-publish_datetime")
    serializer_class = youtubeModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['video_title', 'publish_datetime']
    pagination_class = StandardResultsSetPagination
