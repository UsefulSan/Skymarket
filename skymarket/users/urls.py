from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework import routers

from users.views import UserActivationView

router = routers.SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    # path('', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('<int:pk>/', UserViewSet.as_view({'get': 'retrieve'})),
    path('activate/<uid>/<token>/', UserActivationView.as_view())
] + router.urls

