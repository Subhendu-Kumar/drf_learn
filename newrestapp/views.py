from newrestapp import models, serializer
from rest_framework.response import Response  # type: ignore
from rest_framework import status, viewsets  # type: ignore

# Create your views here.


class waiterViewSet(viewsets.ViewSet):
    def list(self, request):
        wai = models.waiters.objects.all()
        serial = serializer.waiters_serializer(wai, many=True)
        return Response(serial.data)

    def retrieve(self, request, pk=None):
        if pk is not None:
            waiter = models.waiters.objects.get(id=pk)
            serial = serializer.waiters_serializer(waiter)
            return Response(serial.data)
        return Response({"message": "id (pk) is not provided"})

    def create(self, request):
        serial = serializer.waiters_serializer(data=request.body)
        if serial.is_valid():
            serial.save()
            return Response(
                {"message": "data inserted to table"}, status=status.HTTP_201_CREATED
            )
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        waiter = models.waiters.objects.get(id=pk)
        serial = serializer.waiters_serializer(waiter, data=request.body)
        if serial.is_valid():
            serial.save()
            return Response({"message": "data updated"}, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        waiter = models.waiters.objects.get(id=pk)
        serial = serializer.waiters_serializer(waiter, data=request.body, partial=True)
        if serial.is_valid():
            serial.save()
            return Response({"message": "data updated"}, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        waiter = models.waiters.objects.get(id=pk)
        waiter.delete()
        return Response({"message": "record deleted successfully"})
