from rest_framework.viewsets import ModelViewSet
from address.api.serializers import CitySerializer, WardSerializer, DistrictSerializer
from address.models import City, Ward, District
from drf_yasg.utils import swagger_auto_schema
from address.api import swaggers


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    module = ["Address City"]
    http_method_names = ["get"]
    lookup_field = "uid"


class DistrictViewSet(ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    module = ["Address District"]
    model = District
    http_method_names = ["get"]
    lookup_field = "uid"

    def get_queryset(self):
        if self.action == "list":
            if self.request.GET.get("parent") is not None:
                city_id = self.request.GET.get("parent")
                city_obj = City.objects.get(uid=city_id)
                queryset = self.model.objects.filter(parent_code=city_obj)
                return queryset
        return super().get_queryset()

    @swagger_auto_schema(
        tags=["Address District"],
        manual_parameters=swaggers.list_address_params
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class WardViewSet(ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    module = ["Address Ward"]
    model = Ward
    http_method_names = ["get"]
    lookup_field = "uid"

    def get_queryset(self):
        if self.action == "list":
            if self.request.GET.get("parent") is not None:
                district_id = self.request.GET.get("parent")
                district_obj = District.objects.get(uid=district_id)
                queryset = self.model.objects.filter(parent_code=district_obj)
                return queryset
        return super().get_queryset()

    @swagger_auto_schema(
        tags=["Address Ward"],
        manual_parameters=swaggers.list_address_params
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
