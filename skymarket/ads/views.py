from rest_framework import pagination, viewsets

from ads.serializers import AdSerializer, AdMeSerializer

from ads.models import Ad
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ads.permissions import AdsUpdatePermission


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get_permissions(self):
        self.permission_classes = (IsAuthenticated,)
        if self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = (IsAuthenticated, AdsUpdatePermission)
        return tuple(permission() for permission in self.permission_classes)


class AdMeView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdMeSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        self.queryset = self.queryset.filter(author_id__exact=user_id)
        return super().get(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    pass
