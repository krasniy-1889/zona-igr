from django.urls import include, path
from rest_framework import routers

from .views import (
    CommentListAPIView,
    GenresListAPIView,
    PostDetailAPIView,
    PostListAPIView,
)

app_name = "post"


urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="post-list"),
    path("posts/<slug:slug>/", PostDetailAPIView.as_view(), name="post-detail"),
    path("genres/", GenresListAPIView.as_view(), name="genre-list"),
    path("comments/", CommentListAPIView.as_view(), name="comment-list"),
]
