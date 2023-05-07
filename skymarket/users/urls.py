from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework import routers

from skymarket.users.views import UserActivationView, PasswordResetView

router = routers.SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
                  path('activate/<uid>/<token>/', UserActivationView.as_view()),
                  # path('reset_password_confirm/<uid>/<token>/', PasswordResetView.as_view()),
              ] + router.urls
