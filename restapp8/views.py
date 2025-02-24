from restapp8 import models, serializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView  # type: ignore

# Create your views here.


class tester_list(ListAPIView):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer


class tester_crerate(CreateAPIView):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer


class tester_retrieve(RetrieveAPIView):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer


class tester_update(UpdateAPIView):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer


class tester_delete(DestroyAPIView):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer


class tester_list_create(ListCreateAPIView):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer


class tester_retrieve_update(RetrieveUpdateAPIView):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer


class tester_retrieve_delete(RetrieveDestroyAPIView):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer


class tester_retrieve_update_delete(RetrieveUpdateDestroyAPIView):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer
