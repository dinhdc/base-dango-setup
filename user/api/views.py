from rest_framework.viewsets import ModelViewSet
from user.api.serializers import UserSerializer
from user.models import CustomUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["post", "retrieve"]
    module = ["User"]


class UserLoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    module = ["User"]


class UserRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer
    module = ["User"]
