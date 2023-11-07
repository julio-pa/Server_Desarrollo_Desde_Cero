from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
# Imgparsers
from rest_framework.parsers import MultiPartParser, FormParser
# Pagination
from .pagination import SmallSetPagination, MediumSetPagination
# Serializers
from .serializers import PostSerializer
# Models
from .models import Post


# TODO: Make the Post,Get,Update and Delete method for the posts
class PostView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        # print(request.data)
        post_serializer = PostSerializer(data=request.data)
        if post_serializer.is_valid():
            print(post_serializer)
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        if Post.objects.all().exists():
            posts = Post.objects.filter(is_active=True)

            paginator = MediumSetPagination()
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
                serializer.save()
                return Response({'post_updated': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'post doesnt exists'}, status=status.HTTP_400_BAD_REQUEST)


# TODO: Make the Post,Get,Update and Delete method for the comments
# class CommentView(APIView):

# TODO: Make the Post,Get and Delete method for the likes
# class LikesView(APIView):
