from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from apps.post.views import CommentListAPIView, PostListAPIView

# app_name = "api"


# swagger
urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]

# Post urls
urlpatterns += [
    path("posts/", PostListAPIView.as_view(), name="post-list"),
]

# Comments urls
urlpatterns += [
    path("comments/", CommentListAPIView.as_view(), name="comment-list"),
]


# Users urls
urlpatterns += [
    path("auth/", include("apps.user.urls")),
]
