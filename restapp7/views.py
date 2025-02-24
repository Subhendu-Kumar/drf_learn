from restapp7 import models, serializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin  # type: ignore
from rest_framework.generics import GenericAPIView  # type: ignore
from rest_framework import viewsets  # type: ignore

# Create your views here.


class tester_list(GenericAPIView, ListModelMixin):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class tester_create(GenericAPIView, CreateModelMixin):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class tester_retrieve(GenericAPIView, RetrieveModelMixin):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class tester_update(GenericAPIView, UpdateModelMixin):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class tester_delete(GenericAPIView, DestroyModelMixin):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class tester1(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class tester2(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TesterViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions (list, create, retrieve, update, delete)
    """

    queryset = models.tester.objects.all()
    serializer_class = serializer.tester_serializer
