from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView

from .filters import CommentFilter

from .serializers import CommentSerializer, PostSerializer
from .models import Comment, Post


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.annotate(reply_count=Count("children"))
    serializer_class = CommentSerializer
    filterset_class = CommentFilter
    paginate_by = 20


class PostListAPIView(ListAPIView):
    queryset = Post.objects.prefetch_related("genres").annotate(
        comments_count=Count("comments")
    )
    serializer_class = PostSerializer
    # filterset_class = CommentFilter
