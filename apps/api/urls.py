from django.urls import include, path
from rest_framework import routers
from apps.post.views import CommentListAPIView


urlpatterns = [
    path("comments/", CommentListAPIView.as_view(), name="comment-list"),
]
