from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models
from skymarket.users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField



class UserRoles(Enum):
    admin = "admin"
    user = "user"


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    password = models.CharField(max_length=254)
    phone = PhoneNumberField(max_length=128, unique=True, null=True)
    image = models.ImageField(upload_to="image/", null=True)
    role = models.CharField(max_length=40, choices=[UserRoles])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
