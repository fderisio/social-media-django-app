from django.http import Http404
# from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework import generics
# from rest_framework.generics import ListAPIView
#
# from project.api.auth.serializers import UserSerializer, PostItemSerializer
# from project.motion_app.models import User, PostItem
#
#
# class GetFeedView(ListAPIView):
#     serializer_class = PostItemSerializer
#     queryset = PostItem.objects.all()
#
#
# class UsersListView(ListAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


# class GetUserView(APIView):
#     def get(self, user_id):
#         try:
#             return UserSerializer(User.objects.get(id=user_id))
#         except User.DoesNotExist:
#             raise Http404


# class UserDetailView(APIView):
#     def get_object(self, user_id):
#         try:
#             return UserSerializer(User.objects.get(id=user_id))
#         except User.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = UserSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = UserSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class UsersListView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = IsAdminUser
#
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
