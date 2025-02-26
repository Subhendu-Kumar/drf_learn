from newrestapp1 import models, serializer
from rest_framework import viewsets  # type: ignore
from rest_framework.authentication import BasicAuthentication, SessionAuthentication  # type: ignore
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoObjectPermissions, DjangoModelPermissionsOrAnonReadOnly  # type: ignore
from newrestapp1.custompermissions import CustomPermission

# Create your views here.


class singer_view(viewsets.ModelViewSet):
    queryset = models.singer.objects.all()
    serializer_class = serializer.singer_serializer
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    permission_classes = [CustomPermission]
