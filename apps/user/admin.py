from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework.authentication import get_user_model

# Register your models here.


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    pass
