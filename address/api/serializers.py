from address.models import City, Ward, District
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class WardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ward
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = '__all__'
