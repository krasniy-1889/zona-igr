from django.contrib import admin
from rest_framework.authentication import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    pass
