from rest_framework import serializers  # type: ignore
from authapp.models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "name", "password", "password2", "tc"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password2": "Passwords must match."})
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name", "tc"]


class changePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    new_password2 = serializers.CharField()

    def validate(self, data):
        user = self.context.get("user")
        if data["new_password"] != data["new_password2"]:
            raise serializers.ValidationError(
                {"new_password2": "Passwords must match."}
            )
        elif user:
            if not user.check_password(data["old_password"]):
                raise serializers.ValidationError(
                    {"old_password": "Old password is incorrect."}
                )
        else:
            raise serializers.ValidationError({"error": "Something went wrong."})

        return data
