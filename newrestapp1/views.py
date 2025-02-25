from newrestapp1 import models, serializer
from rest_framework import viewsets  # type: ignore
from rest_framework.authentication import BasicAuthentication  # type: ignore
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser  # type: ignore

# Create your views here.


class singer_view(viewsets.ModelViewSet):
    queryset = models.singer.objects.all()
    serializer_class = serializer.singer_serializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]
