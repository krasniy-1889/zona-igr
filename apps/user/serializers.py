from rest_framework import serializers
from rest_framework.authentication import get_user_model
from apps.user.models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "bio",
            "location",
            "birth_date",
        ]


class UserWithProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "is_superuser",
            "is_staff",
            "is_active",
            "profile",
        ]

        def get_profile(self, obj):
            return ProfileSerializer(obj.profile).data


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
        ]

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)  # type: ignore
