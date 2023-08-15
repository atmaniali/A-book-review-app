from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializer import UserSerializer
from .permission import IsUserOwnerORGetOrPost


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerORGetOrPost]
