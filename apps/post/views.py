from django.db.models import Count
from rest_framework.generics import ListAPIView

from .filters import CommentFilter

from .serializers import CommentSerializer, PostSerializer
from .models import Comment, Post


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.annotate(reply_count=Count("children"))
    serializer_class = CommentSerializer
    filterset_class = CommentFilter
