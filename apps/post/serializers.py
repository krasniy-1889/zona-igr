from re import M
from loguru import logger
from rest_framework import serializers, viewsets

from .models import Comment, Genre, Post


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    reply_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "text",
            "parent",
            "created_at",
            "updated_at",
            "reply_count",
        ]


class PostSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True)
    comments_count = serializers.IntegerField(read_only=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "poster",
            "voiceover_language",
            "interface_language",
            "developer",
            "content",
            "operating_system",
            "processor",
            "memory",
            "video_card",
            "sound_card",
            "disk_space",
            "genres",
            # "comments",
            "comments_count",
            "created_at",
            "updated_at",
        ]

    # def get_comments(self, obj):
    #     serializer = CommentSerializer(obj.comments.all(), many=True)
    #     return serializer.data

    def get_genres(self, obj):
        serializer = GenreSerializer(obj.genres.all(), many=True)
        return serializer.data
