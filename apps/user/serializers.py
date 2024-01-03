from rest_framework import serializers
from rest_framework.authentication import get_user_model


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
            "is_staff",
            "is_active",
            "last_login",
            "url",
        ]
