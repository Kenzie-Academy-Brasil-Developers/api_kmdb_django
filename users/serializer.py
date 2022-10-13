from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ["id", "updated_at", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}
        exclude = [
            "last_login",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
        ]

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
