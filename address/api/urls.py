from rest_framework.routers import DefaultRouter
from address.api.views import CityViewSet, DistrictViewSet, WardViewSet

urlpatterns = []
router = DefaultRouter()
router.register(r'cities', CityViewSet, basename="city manager")
router.register(r'districts', DistrictViewSet, basename="district manager")
router.register(r'wards', WardViewSet, basename="wards manager")
urlpatterns += router.urls
