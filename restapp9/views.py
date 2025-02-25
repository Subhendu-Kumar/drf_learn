from restapp9 import models, serializer
from rest_framework import viewsets  # type: ignore
from rest_framework.authentication import SessionAuthentication  # type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly  # type: ignore


# Create your views here.


class tester_view(viewsets.ModelViewSet):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
