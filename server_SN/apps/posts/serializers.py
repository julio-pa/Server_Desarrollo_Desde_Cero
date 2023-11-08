from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'slug',
            'text',
            'image',
            'is_active',
            'created',
            'modified',
            'deleted',
        ]
        extra_kwargs = {'user': {'required': False}}


class CommentSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'user_id',
            'post_id',
            'text',
            'is_active',
            'created',
            'modified',
            'deleted',
        ]
        extra_kwargs = {'user_id': {'required': False},
                        'post_id': {'required': False}}


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like_post
        fields = [
            'id'
            'user_id'
            'post_id'
        ]
