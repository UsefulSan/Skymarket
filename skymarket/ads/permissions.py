# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework.permissions import BasePermission

from ads.models import Ad


class AdsUpdatePermission(BasePermission):
    message = "У вас нет прав на редактирование чужих объявлений =("

    def has_permission(self, request, view):
        author_id = Ad.objects.get(pk=view.kwargs["pk"]).author_id
        if author_id == request.user.id or request.user.role == 'admin':
            return True
        return False