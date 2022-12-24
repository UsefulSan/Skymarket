from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets

from ads.serializers import AdSerializer, AdMeSerializer, CommentSerializer

from ads.models import Ad, Comment

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.permissions import AdUpdatePermission, CommentUpdatePermission


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get_permissions(self):
        self.permission_classes = (IsAuthenticated,)
        if self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = (IsAuthenticated, AdUpdatePermission)
        elif self.action == 'list':
            self.permission_classes = (AllowAny,)
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
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.select_related('author').select_related('ad_pk').filter(ad_pk__id=self.kwargs['ad_pk'])

    def perform_create(self, serializer):
        serializer.save(ad_pk=get_object_or_404(Ad, id=self.kwargs['ad_pk']))

    def get_permissions(self):
        self.permission_classes = (IsAuthenticated,)
        if self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = (IsAuthenticated, CommentUpdatePermission)
        return tuple(permission() for permission in self.permission_classes)
