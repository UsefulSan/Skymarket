from enum import Enum

from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
# from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(Enum):
    admin = "admin"
    user = "user"


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    role = models.CharField(max_length=40, choices=[UserRoles])
    image = models.ImageField(upload_to="image/", null=True)
