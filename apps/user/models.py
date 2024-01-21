from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import get_user_model

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user_users"
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class UserProfile(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username  # type: ignore
