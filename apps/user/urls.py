from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.user.views import UserCreateView, UserGetMe, UserListAPIView

app_name = "user"

urlpatterns = [
    path("users/", UserListAPIView.as_view(), name="user-list"),
    path("register/", UserCreateView.as_view(), name="user-register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", UserGetMe.as_view(), name="me"),
]
