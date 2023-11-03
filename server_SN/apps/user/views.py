from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
# Imgparsers
from rest_framework.parsers import MultiPartParser, FormParser
# Pagination
from .pagination import SmallSetPagination
# Models
from .models import UserFollowing, UserAccount, Profile
# Serializers
from .serializers import ProfileSerializer, UserFollowingSerializer, UserSerializer
# Create your views here.
# TODO:Create view to delete user(Only change "is_active" to false)


class FollowingSystemView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        follow_serializer = UserFollowingSerializer(data=request.data)

        if follow_serializer.is_valid():
            follow_serializer.save()
            return Response(follow_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(follow_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, follow_id, format=None):
        if UserFollowing.objects.filter(id=follow_id).exists():
            follow = UserFollowing.objects.get(id=follow_id)
            follow.delete()
            return Response({'follow': 'follow delete successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'follow doent exist'}, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if UserAccount.objects.all().exists():

            users = UserAccount.objects.all()

            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(users, request)
            serializer = UserSerializer(results, many=True)

            return paginator.get_paginated_response({'users': serializer.data})
        else:
            return Response({'error': 'No users found'}, status=status.HTTP_404_NOT_FOUND)


class ProfileUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, user_id, format=None):
        if UserAccount.objects.filter(id=user_id).exists():
            profile = Profile.objects.get(user=user_id)
            user = UserAccount.objects.get(id=user_id)
            following = UserFollowingSerializer(
                user.following.all(), many=True)
            followers = UserFollowingSerializer(
                user.followers.all(), many=True)
            serializer = ProfileSerializer(profile)

            return Response({'profile': serializer.data,
                             'following': following.data,
                             'followers': followers.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, format=None):
        profile_data = self.request.data

        user_id = profile_data['id']

        print(profile_data)

        profile = Profile.objects.get(user=user_id)
        user = UserAccount.objects.get(id=user_id)
        serializer = ProfileSerializer(profile, data=profile_data)

        if 'username' in profile_data:
            user.username = profile_data['username']
            user.save()
        else:
            pass

        if serializer.is_valid():
            serializer.save()
            return Response({'profile_updated': serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, account_id, format=None):
        if UserAccount.objects.filter(id=account_id).exists():
            account = UserAccount.objects.get(id=account_id)
            if account.is_active is True:
                account.is_active = False
                account.save()
            return Response({'account': 'account delete successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'account doent exists'}, status=status.HTTP_400_BAD_REQUEST)
