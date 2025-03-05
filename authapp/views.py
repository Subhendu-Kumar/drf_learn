from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from rest_framework.views import APIView  # type: ignore
from authapp.serializer import user_serializer, user_login_serializer
from django.contrib.auth import authenticate

# Create your views here.


class user_registration_view(APIView):
    def post(self, request):
        serializer = user_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Registration successful!"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class user_login_view(APIView):
    def post(self, request):
        serializer = user_login_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=email, password=password)

            if user is not None:
                user_data = {
                    "id": user.id,
                    "email": user.email,
                    "name": user.name,
                }
                return Response(
                    {"message": "Login successful!", "user": user_data},
                    status=status.HTTP_200_OK,
                )

            return Response(
                {
                    "message": f"User with email {email} not found or incorrect password!"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
