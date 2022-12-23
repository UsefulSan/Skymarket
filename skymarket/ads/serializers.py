from rest_framework import serializers

from ads.models import Ad

from users.models import User


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


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
