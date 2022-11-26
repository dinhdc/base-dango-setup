from rest_framework.routers import DefaultRouter
from user.api.views import UserViewSet, UserLoginView, UserRefreshView, UserViewProfile

from django.urls import path

urlpatterns = [
    path('token/', UserLoginView.as_view(), name='token_obtain_pair'),
    path('profile/', UserViewProfile.as_view(), name='user_profile'),
    path('token/refresh/', UserRefreshView.as_view(), name='token_refresh'),
]
router = DefaultRouter()
router.register(r'users', UserViewSet, basename="User Controller")
urlpatterns += router.urls
