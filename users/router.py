from rest_framework import routers

from .viesets import UserViewSet

router = routers.DefaultRouter()

router.register('user', UserViewSet)