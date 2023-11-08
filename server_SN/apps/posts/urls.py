from django.urls import path

from .views import *

urlpatterns = [
    # Posts endpoints
    path('create', PostView.as_view()),
    path('list', PostView.as_view()),
    path('edit', PostView.as_view()),
    path('delete/<post_id>', PostView.as_view()),
    # Comment endpoints
    path('comment/create', CommentView.as_view()),
    path('comment/list/<id_post>', CommentView.as_view()),
    path('comment/edit', CommentView.as_view()),
    path('comment/delete/<comment_id>', CommentView.as_view()),
    # like endpoints
    path('like/create', LikesView.as_view()),
    path('like/delete/<like_id>', LikesView.as_view()),
]
