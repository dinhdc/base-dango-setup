from django.test import TestCase
from rest_framework.test import APIRequestFactory
from address.models import City, District, Ward
from user.models import CustomUser
from rest_framework import status
from rest_framework.test import APIClient


class TestUserModel(TestCase):

    factory = APIRequestFactory()
    apiClient = APIClient()
    USER_URL = {
        "register": "http://127.0.0.1:8000/api/users/",
        "login": "http://127.0.0.1:8000/api/token/",
        "profile": "http://127.0.0.1:8000/api/profile/",
    }
    USER_FIELDS = ["email",
                   "username",
                   "cccd",
                   "date_of_birth",
                   "sex",
                   "city",
                   "district",
                   "ward",
                   "phone_number",
                   "is_active",
                   "is_staff", ]

    def setUp(self):
        city = City.objects.create(
            name="Hà Nội",
            slug="ha-noi",
            type="thanh-pho",
            name_with_type="Thành phố Hà Nội",
            code=1)
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
        ward = Ward.objects.create(
            name="Trúc Bạch",
            slug="truc-bach",
            type="phuong",
            name_with_type="Phường Trúc Bạch",
            path="Trúc Bạch, Ba Đình, Hà Nội",
            path_with_type="Phường Trúc Bạch, Quận Ba Đình, Thành phố Hà Nội",
            code=4,
            parent_code=district
        )

        CustomUser.objects.create_superuser(
            email="zedpro2k@gmail.com",
            username="congdinh2k",
            password="123456a@",
            cccd="123123123",
            date_of_birth="2000-01-01",
            sex="male",
            city=city,
            district=district,
            ward=ward,
            phone_number="2131312312",
            is_active=True,
            is_staff=True
        )

    def test_create_new_user(self):
        url = self.USER_URL["register"]
        request_data = {
            "email": "zedpro2k@gmail.com",
            "username": "zedpro2k",
            "password": "123456a@",
            "cccd": "123123123",
            "dateOfBirth": "2000-01-01",
            "sex": "male",
            "city": City.objects.first().uid,
            "district":  District.objects.first().uid,
            "ward": Ward.objects.first().uid,
            "phoneNumber": "2131312312"
        }
        response = self.apiClient.post(url, data=request_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        del request_data['password']
        del request_data["dateOfBirth"]
        del request_data["phoneNumber"]
        del request_data["city"]
        del request_data["district"]
        del request_data["ward"]
        self.assertDictContainsSubset(request_data, response.data)

    def test_login_user_with_username_and_password(self):
        url = self.USER_URL["login"]
        request_data = {
            "username": "congdinh2k",
            "password": "123456a@"
        }
        response = self.apiClient.post(url, data=request_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data["access"], "")
        self.assertNotEqual(response.data["refresh"], "")

    def test_login_user_with_username_and_password_not_match(self):
        url = self.USER_URL["login"]
        request_data = {
            "username": "congdinh2k",
            "password": "12345611a@"
        }
        response = self.apiClient.post(url, data=request_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_profile_user(self):
        url = self.USER_URL["login"]
        user = CustomUser.objects.first()
        request_data = {
            "username": user.username,
            "password": "123456a@"
        }
        response = self.apiClient.post(url, data=request_data)
        access = response.data["access"]
        self.apiClient.credentials(HTTP_AUTHORIZATION='Bearer ' + access)
        self.assertNotEqual(access, "")
        profile = self.USER_URL["profile"]
        profile_response = self.apiClient.get(profile)
        self.assertEqual(profile_response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.username, profile_response.data["username"])
        self.assertEqual(user.cccd, profile_response.data["cccd"])
        self.assertEqual(user.phone_number, profile_response.data["phone_number"])
        self.assertEqual(user.email, profile_response.data["email"])
        self.assertEqual(str(user.city.uid), profile_response.data["city"]["uid"])
        self.assertEqual(str(user.district.uid), profile_response.data["district"]["uid"])
        self.assertEqual(str(user.ward.uid), profile_response.data["ward"]["uid"])
