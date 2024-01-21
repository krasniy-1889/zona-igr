from django.db.models import Count
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .filters import CommentFilter, PostFilter
from .models import Comment, Genre, Post
from .serializers import CommentSerializer, GenreSerializer, PostSerializer


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
    permission_classes = [IsAuthenticated]
    filterset_class = PostFilter


class PostDetailAPIView(RetrieveAPIView):
    queryset = (
        Post.objects.select_related("developer")
        .prefetch_related("genres")
        .annotate(
            # comments_count=Count("comments"),
            likes_count=Count("likes", distinct=True),
            dislikes_count=Count("dislikes", distinct=True),
        )
    )
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"


class PostCreateAPIView(APIView):
    model = Post
    serializer_class = PostSerializer

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


# Genres
class GenresListAPIView(ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    paginate_by = 100
