from django.urls import include, path
from rest_framework import routers
from apps.post.views import CommentListAPIView, PostListAPIView

# Post urls
urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="post-list"),
]

# Comments urls
urlpatterns += [
    path("comments/", CommentListAPIView.as_view(), name="comment-list"),
]
