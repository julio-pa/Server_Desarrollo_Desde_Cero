from django.urls import path

from .views import *

urlpatterns = [
    path('profile/<user_id>', ProfileUserView.as_view()),
    path('follow', FollowingSystemView.as_view()),
    path('update', UpdateProfileView.as_view()),
]
