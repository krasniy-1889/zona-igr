from django_filters import FilterSet, CharFilter, NumberFilter
from .models import Comment


class CommentFilter(FilterSet):
    parent_id = NumberFilter(field_name="parent_id")

    class Meta:
        model = Comment
        fields = ["parent_id"]
