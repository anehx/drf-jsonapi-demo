from demo_api       import models
from django_filters import FilterSet


class PostFilterSet(FilterSet):
    class Meta:
        model = models.Post


class CommentFilterSet(FilterSet):
    class Meta:
        model = models.Comment
