from rest_framework import routers

from .viewsets import UserViewSet

router = routers.DefaultRouter()

router.register('user', UserViewSet)