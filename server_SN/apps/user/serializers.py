from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import *

from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            'id',
            'username',
            'email',
            'is_active',
            'is_staff',
        ]


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = [
#             'id',
#             'user',
#             'img_profile',
#             'banner',
#             'bio',
#             'joined',
#             'following',
#             'followers',
#         ]
