from rest_framework import serializers  # type: ignore
from authapp.models import User


class user_serializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "name", "password", "password2", "tc"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True},
            "name": {"required": True},
        }

    def validate_email(self, value):
        """Check if email is unique."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, data):
        """Check if passwords match."""
        if data.get("password") != data.get("password2"):
            raise serializers.ValidationError({"password2": "Passwords must match."})
        return data

    def create(self, validated_data):
        """Create user with hashed password."""
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user


class user_login_serializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
