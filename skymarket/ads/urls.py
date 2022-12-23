from django.urls import include, path

from ads.views import AdViewSet, AdMeView
from rest_framework import routers



# TODO настройка роутов для модели

router = routers.SimpleRouter()
router.register('', AdViewSet)

urlpatterns = [
    path('me/', AdMeView.as_view())

] + router.urls
