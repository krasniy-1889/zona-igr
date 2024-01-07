from django.db.models import Count
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .filters import CommentFilter
from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.annotate(reply_count=Count("children")).select_related(
        "user"
    )
    serializer_class = CommentSerializer
    filterset_class = CommentFilter


class PostListAPIView(ListAPIView):
    queryset = (
        Post.objects.select_related("developer")
        .prefetch_related("genres")
        .annotate(
            comments_count=Count("comments"),
            likes_count=Count("likes", distinct=True),
            dislikes_count=Count("dislikes", distinct=True),
        )
    )
    serializer_class = PostSerializer
    # authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
