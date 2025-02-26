from newrestapp2 import models, serializer
from rest_framework import viewsets  # type: ignore
from rest_framework.authentication import TokenAuthentication  # type: ignore
from rest_framework.permissions import IsAuthenticated  # type: ignore

# Create your views here.


class dancer_view(viewsets.ModelViewSet):
    queryset = models.dancer.objects.all()
    serializer_class = serializer.dancer_serializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
