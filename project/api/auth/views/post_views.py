from rest_framework.generics import ListAPIView

from project.api.auth.serializers import PostItemSerializer
from project.motion_app.models import PostItem


class GetFeedView(ListAPIView):
    serializer_class = PostItemSerializer
    queryset = PostItem.objects.all()
