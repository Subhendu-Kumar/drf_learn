from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from rest_framework.views import APIView  # type: ignore
from rest_framework.permissions import IsAuthenticated  # type: ignore
from authapp.serializer import (
    UserSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
)
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken  # type: ignore


# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Registration successful!"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=email, password=password)

            if user:
                token = get_tokens_for_user(user)
                return Response(
                    {"message": "Login successful!", "token": token},
                    status=status.HTTP_200_OK,
                )

            return Response(
                {"message": "Invalid email or password!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(
            request.user, context={"request": request}
        )  # Serialize user instance
        return Response(serializer.data, status=status.HTTP_200_OK)
