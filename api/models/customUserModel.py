# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from api.models.userManager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=255, blank=True, null=True)
    last_name = models.CharField(_("last name"), max_length=255, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)
    is_mentor = models.BooleanField()
    is_mentee = models.BooleanField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
