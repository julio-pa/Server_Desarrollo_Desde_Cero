from django.urls import path

from .views import *

urlpatterns = [
    path('create', PostView.as_view()),
    path('list', PostView.as_view()),
    path('edit', PostView.as_view()),
    path('delete/<post_id>', PostView.as_view()),
    path('comment/create', CommentView.as_view()),
    path('comment/list/<id_post>', CommentView.as_view()),
]
