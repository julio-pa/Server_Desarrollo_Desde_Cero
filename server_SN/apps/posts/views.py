from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
# timezone
from django.utils import timezone
# Imgparsers
from rest_framework.parsers import MultiPartParser, FormParser
# Pagination
from .pagination import MediumSetPagination, LargeSetPagination
# Serializers
from .serializers import PostSerializer, CommentSerializer, LikesSerializer
# Models
from .models import Post, Comment, Like_post


class PostView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        # print(request.data)
        post_serializer = PostSerializer(data=request.data)
        if post_serializer.is_valid():
            # print(post_serializer)
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        if Post.objects.all().exists():
            posts = Post.objects.filter(is_active=True)

            paginator = LargeSetPagination()
            results = paginator.paginate_queryset(posts, request)

            serializer = PostSerializer(results, many=True)

            return paginator.get_paginated_response({'posts': serializer.data})
        else:
            return Response({'error': 'No posts found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, format=None):
        post_data = request.data
        post_id = post_data['id']

        if Post.objects.filter(id=post_id).exists():

            current_post = Post.objects.get(id=post_id)
            serializer = PostSerializer(current_post, data=post_data)

            if serializer.is_valid():
                current_post.modified = timezone.now()
                current_post.save()
                serializer.save()
                return Response({'post_updated': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'post doesnt exists'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, format=None):
        if Post.objects.filter(id=post_id, is_active=True).exists():
            current_post = Post.objects.get(id=post_id)

            current_post.is_active = False
            current_post.deleted = timezone.now()

            current_post.save()

            return Response({'post': 'post delete successfully'}, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'post doesnt exists'}, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'comment': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id_post, format=None):
        if Comment.objects.all().exists():
            comments = Comment.objects.filter(is_active=True, post_id=id_post)

            paginator = MediumSetPagination()
            results = paginator.paginate_queryset(comments, request)

            serializer = CommentSerializer(results, many=True)

            return paginator.get_paginated_response({'comments': serializer.data})
        else:
            return Response({'error': 'No comments found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, format=None):
        comment_data = request.data
        comment_id = comment_data['id']

        if Comment.objects.filter(id=comment_id).exists():

            current_comment = Comment.objects.get(id=comment_id)
            # print(current_comment)
            serializer = CommentSerializer(current_comment, data=comment_data)
            if serializer.is_valid():
                current_comment.modified = timezone.now()
                current_comment.save()
                serializer.save()
                return Response({'comment_edited': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'comment doesnt exists'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id, format=None):
        if Comment.objects.filter(id=comment_id, is_active=True).exists():
            current_comment = Comment.objects.get(id=comment_id)

            current_comment.is_active = False
            current_comment.deleted = timezone.now()

            current_comment.save()

            return Response({'comment': 'comment delete successfully'}, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'comment doesnt exists'}, status=status.HTTP_400_BAD_REQUEST)


# TODO: Make the Post,Get and Delete method for the likes
class LikesView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LikesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'like': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, like_id, format=None):
        if Like_post.objects.filter(id=like_id).exists():
            follow = Like_post.objects.get(id=like_id)
            follow.delete()
            return Response({'like': 'like delete successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'follow doent exist'}, status=status.HTTP_400_BAD_REQUEST)
