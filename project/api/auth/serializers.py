# from django.contrib.auth import get_user_model
from rest_framework import serializers
from ...motion_app.models import PostItem, User

# In case there is no User model, a rest_framework model can be used:
# User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'name', 'email'
        ]
        read_only_fields = fields

    def get_post_count(self, user):
        return user.posts.count()

    def get_fame_index(self, user):
        return sum([p.likes.count() for p in user.posts.all()])


class PostItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PostItem
        fields = [
            'id', 'title', 'content', 'created', 'user'
        ]
        read_only_fields = ['user']
