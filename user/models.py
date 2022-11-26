from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from address.models import City, District, Ward
import uuid


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError(_('The Username must be set'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'))
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    username = models.CharField(max_length=255, unique=True)
    cccd = models.CharField(max_length=20,)
    date_of_birth = models.DateField(null=True)
    sex = models.CharField(max_length=10)
    city = models.ForeignKey(City, to_field="uid",
                             on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(
        District, to_field="uid", on_delete=models.SET_NULL, null=True)
    ward = models.ForeignKey(Ward, to_field="uid",
                             on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
