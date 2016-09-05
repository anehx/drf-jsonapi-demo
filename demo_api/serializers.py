from demo_api                import models
from rest_framework_json_api import serializers


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.ResourceRelatedField(
        queryset=models.Comment.objects.all(),
        many=True
    )

    class Meta:
        model = models.Post


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.ResourceRelatedField(
        queryset=models.Post.objects.all()
    )

    class Meta:
        model = models.Comment


PostSerializer.included_serializers = {
    'comments': CommentSerializer
}
