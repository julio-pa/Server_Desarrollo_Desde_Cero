from django.urls import path

from .views import *

urlpatterns = [
    path('create', PostView.as_view()),
    path('list', PostView.as_view()),
    path('edit', PostView.as_view()),
]
