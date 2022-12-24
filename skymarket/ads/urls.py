from django.urls import include, path

from ads.views import AdViewSet, AdMeView, CommentViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', AdViewSet)

urlpatterns = [
                  path('me/', AdMeView.as_view()),
                  path('<int:ad_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
                  path('<int:ad_pk>/comments/<int:pk>/', CommentViewSet.as_view({"get": "retrieve",
                                                                                 'patch': 'update',
                                                                                 'delete': 'destroy'}))
              ] + router.urls
