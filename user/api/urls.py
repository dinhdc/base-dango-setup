from rest_framework.routers import DefaultRouter
from user.api.views import UserViewSet, UserLoginView, UserRefreshView

from django.urls import path

urlpatterns = [
    path('token/', UserLoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', UserRefreshView.as_view(), name='token_refresh'), ]
router = DefaultRouter()
router.register(r'users', UserViewSet, basename="User Controller")
urlpatterns += router.urls
