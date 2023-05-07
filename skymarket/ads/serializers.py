from rest_framework import serializers

from skymarket.ads.models import Ad, Comment
from skymarket.users.models import User


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='id', queryset=User.objects.all(), required=False)
    author_last_name = serializers.CharField(source='author.last_name', required=False)
    author_first_name = serializers.CharField(source='author.first_name', required=False)

    class Meta:
        model = Ad
        fields = ["id", "image", "title", "price", "description", 'author_first_name', 'author_last_name', 'author']

    def create(self, validated_data):
        request = self.context.get('request', None)
        return Ad.objects.create(**validated_data, author_id=request.user.id)


class AdMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='id', queryset=User.objects.all(), required=False)
    author_last_name = serializers.CharField(source='author.last_name', required=False)
    author_first_name = serializers.CharField(source='author.first_name', required=False)
    ad_pk = serializers.SlugRelatedField(slug_field='id', queryset=Ad.objects.all(), required=False)
    author_image = serializers.ImageField(source='author.image', required=False)

    class Meta:
        model = Comment
        fields = ["pk", "text", "author", "created_at", 'author_first_name',
                  'author_last_name', 'ad_pk', 'author_image']

    def is_valid(self, raise_exception=False):
        self._items = self.initial_data.pop("author", None)
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        request = self.context.get('request', None)
        return Comment.objects.create(**validated_data, author_id=request.user.id)
