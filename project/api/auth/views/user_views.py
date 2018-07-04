from rest_framework.generics import ListAPIView

from project.api.auth.serializers import UserSerializer
from project.motion_app.models import User


class UsersListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()