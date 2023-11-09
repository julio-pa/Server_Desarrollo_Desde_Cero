from rest_framework import serializers
from .models import *
from apps.user.serializers import ProfileSerializer


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
            'likes',
            'created',
            'modified',
            'deleted',
        ]
        extra_kwargs = {'user': {'required': False}}

    def to_representation(self, instance):
        response = super().to_representation(instance)

        likes_count = Like_post.objects.filter(post_id=instance.id).count()
        response['likes'] = likes_count
        response['user'] = ProfileSerializer(instance.user).data
        instance.save()
        return response


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

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response['user_id'] = ProfileSerializer(instance.user_id).data
        instance.save()
        return response


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like_post
        fields = [
            'id',
            'user_id',
            'post_id',
        ]
