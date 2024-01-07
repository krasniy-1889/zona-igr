from django_filters import FilterSet, NumberFilter

from .models import Comment


class CommentFilter(FilterSet):
    parent_id = NumberFilter(field_name="parent_id")
    user_id = NumberFilter(field_name="user_id")

    class Meta:
        model = Comment
        fields = [
            "parent_id",
            "user_id",
        ]
