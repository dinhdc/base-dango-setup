from rest_framework.viewsets import ModelViewSet
from user.api.serializers import UserSerializer, UserCreateSerializer
from user.models import CustomUser
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    http_method_names = ["post", "retrieve"]
    module = ["User"]


class UserLoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    module = ["User"]


class UserRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer
    module = ["User"]


class UserViewProfile(APIView):

    permission_classes = [IsAuthenticated]
    module = ["User"]

    @swagger_auto_schema(tags=["User"])
    def get(self, request):
        user = self.request.user
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
