from django_filters import FilterSet, NumberFilter, CharFilter, MultipleChoiceFilter

from .models import Comment, Post


class CommentFilter(FilterSet):
    parent_id = NumberFilter(field_name="parent_id")
    user_id = NumberFilter(field_name="user_id")

    class Meta:
        model = Comment
        fields = [
            "parent_id",
            "user_id",
        ]


class PostFilter(FilterSet):
    genre = CharFilter(field_name="genres__name", lookup_expr="exact")

    class Meta:
        model = Post
        fields = [
            "genre",
        ]
