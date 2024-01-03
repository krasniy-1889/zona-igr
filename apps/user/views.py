from rest_framework import viewsets
from rest_framework.authentication import get_user_model

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
