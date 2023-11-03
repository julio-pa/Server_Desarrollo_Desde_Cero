from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
# Imgparsers
from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import UserFollowing, UserAccount, Profile
from .serializers import ProfileSerializer, UserFollowingSerializer
# Create your views here.

# TODO:Make the Delete follow method


class FollowingSystemView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        follow_serializer = UserFollowingSerializer(data=request.data)

        if follow_serializer.is_valid():
            follow_serializer.save()
            return Response(follow_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(follow_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO:Make the update profile method
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

            return Response({'profile': serializer.data, 'following': following.data, 'followers': followers.data}, status=status.HTTP_200_OK)
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
        serializer = ProfileSerializer(profile, data=profile_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'profile_updated': serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
