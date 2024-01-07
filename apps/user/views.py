from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.authentication import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserGetMe(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return JsonResponse(serializer.data)
