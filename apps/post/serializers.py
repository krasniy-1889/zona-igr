from loguru import logger
from rest_framework import serializers, viewsets

from apps.user.serializers import UserSerializer

from .models import Comment, Genre, Post


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    reply_count = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "text",
            "created_at",
            "updated_at",
            "reply_count",
            "user",
        ]


class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    dislikes_count = serializers.IntegerField(read_only=True)
    genres = GenreSerializer(many=True)
    developer = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "poster",
            "voiceover_language",
            "interface_language",
            "developer",
            "content",
            # System requirements
            "operating_system",
            "processor",
            "memory",
            "video_card",
            "sound_card",
            "disk_space",
            # Likes and dislikes
            "likes_count",
            "dislikes_count",
            "created_at",
            "updated_at",
            "comments_count",
            "genres",
        ]

    def get_genres(self, obj):
        serializer = GenreSerializer(obj.genres.all(), many=True)
        return serializer.data

    def get_developer(self, obj):
        return obj.developer.name
