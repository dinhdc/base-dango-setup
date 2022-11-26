from rest_framework import serializers
from user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = ('id', 'groups', 'user_permissions',)
        depth = 1
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            'last_login': {
                'read_only': True
            },
            'is_superuser': {
                'read_only': True
            },
            'is_staff': {
                'read_only': True
            },
            'is_active': {
                'read_only': True
            },
            'date_joined': {
                'read_only': True
            },

        }

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        password = validated_data["password"]
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserRefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
