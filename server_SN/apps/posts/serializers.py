from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'text',
            'image',
            'is_active',
            'created',
            'modified',
            'deleted',
        ]


class CommentSerializer(serializers.ModelSerializer):
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


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like_post
        fields = [
            'id'
            'user_id'
            'post_id'
        ]
