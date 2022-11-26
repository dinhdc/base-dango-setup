from django.test import TestCase
from rest_framework.test import APIRequestFactory
from address.models import City, Ward, District
from rest_framework import status
from rest_framework.test import APIClient


class TestAddressModel(TestCase):

    factory = APIRequestFactory()
    apiClient = APIClient()

    def setUp(self):
        city = City.objects.create(name="Hà Nội",
                                   slug="ha-noi",
                                   type="thanh-pho",
                                   name_with_type="Thành phố Hà Nội",
                                   code=1)
        city2 = City.objects.create(name="Hà Nội v2",
                                    slug="ha-noi-2",
                                    type="thanh-pho",
                                    name_with_type="Thành phố Hà Nội",
                                    code=2)
        district = District.objects.create(
            name="Ba Đình",
            slug="ba-dinh",
            type="quan",
            name_with_type="Quận Ba Đình",
            path="Ba Đình, Hà Nội",
            path_with_type="Quận Ba Đình, Thành phố Hà Nội",
            code=1,
            parent_code=city
        )
        district2 = District.objects.create(
            name="Ba Đình v2",
            slug="ba-dinh",
            type="quan",
            name_with_type="Quận Ba Đình",
            path="Ba Đình, Hà Nội",
            path_with_type="Quận Ba Đình, Thành phố Hà Nội",
            code=1,
            parent_code=city2
        )
        Ward.objects.create(
            name="Trúc Bạch",
            slug="truc-bach",
            type="phuong",
            name_with_type="Phường Trúc Bạch",
            path="Trúc Bạch, Ba Đình, Hà Nội",
            path_with_type="Phường Trúc Bạch, Quận Ba Đình, Thành phố Hà Nội",
            code=4,
            parent_code=district
        )
        Ward.objects.create(
            name="Trúc Bạch v2",
            slug="truc-bach",
            type="phuong",
            name_with_type="Phường Trúc Bạch",
            path="Trúc Bạch, Ba Đình, Hà Nội",
            path_with_type="Phường Trúc Bạch, Quận Ba Đình, Thành phố Hà Nội",
            code=4,
            parent_code=district2
        )

    def test_get_list_city(self):
        url = "http://127.0.0.1:8000/api/address/cities/"
        totals = City.objects.all().count()
        response = self.apiClient.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], totals)

    def test_get_list_district(self):
        url = "http://127.0.0.1:8000/api/address/districts/"
        totals = District.objects.all().count()
        response = self.apiClient.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], totals)

    def test_get_list_district_with_filter(self):
        city_first = City.objects.first()
        city_first_uid = city_first.uid
        url = "http://127.0.0.1:8000/api/address/districts/?parent={0}".format(
            city_first_uid)
        totals = District.objects.filter(parent_code=city_first).count()
        response = self.apiClient.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], totals)
