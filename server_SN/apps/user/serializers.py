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


# Following system serializers
class UserFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = [
            'id',
            'user_id',
            'following_user_id',
            'created'
        ]


class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = ("id", "following_user_id", "created")


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("id", "user_id", "created")

# TODO:Create the to_representation function


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "img_profile",
            "bio",
            "joined",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        instance.save()
        return response
