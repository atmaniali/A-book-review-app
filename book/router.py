from rest_framework import routers

from .viewsets import BookViewSet, ReviewViewSet

router = routers.DefaultRouter()

router.register(r'book', BookViewSet)
router.register(r'review', ReviewViewSet)