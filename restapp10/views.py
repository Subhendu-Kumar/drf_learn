from restapp9 import models, serializer
from rest_framework import viewsets  # type: ignore


# Create your views here.


class tester_view(viewsets.ModelViewSet):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer
