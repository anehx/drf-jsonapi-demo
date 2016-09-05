from demo_api       import serializers, models, filters
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset         = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    filter_class     = filters.PostFilterSet


class CommentViewSet(viewsets.ModelViewSet):
    queryset         = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    filter_class     = filters.CommentFilterSet
