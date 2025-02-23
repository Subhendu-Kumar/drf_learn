from rest_framework.decorators import api_view  # type: ignore
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from restapp6.serializer import trainer_serializer
from restapp6.models import trainer


@api_view(["GET", "POST", "PUT", "DELETE"])
@csrf_exempt
def ter_data(request):
    if request.method == "GET":
        if request.data:
            trainer_id = request.data.get("id", None)
            if trainer_id is not None:
                try:
                    ter = trainer.objects.get(id=trainer_id)
                    serial = trainer_serializer(ter)
                    return Response(serial.data, status=status.HTTP_200_OK)
                except trainer.DoesNotExist:
                    return Response(
                        {"error": "trainer not found"}, status=status.HTTP_404_NOT_FOUND
                    )
        ter = trainer.objects.all()
        serial = trainer_serializer(ter, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        data = request.data
        serializer = trainer_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Data inserted successfully", "success": True},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        trainer_id = request.data.get("id", None)
        if trainer_id is None:
            return Response(
                {"error": "ID is required for update"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            ter = trainer.objects.get(id=trainer_id)
            serial = trainer_serializer(ter, data=py_data, partial=True)
            if serial.is_valid():
                serial.save()
                return Response(
                    {"message": "Data updated successfully", "success": True},
                    status=status.HTTP_200_OK,
                )
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except trainer.DoesNotExist:
            return Response(
                {"error": "trainer not found"}, status=status.HTTP_404_NOT_FOUND
            )

    elif request.method == "DELETE":
        trainer_id = request.data.get("id", None)
        if trainer_id is None:
            return Response(
                {"error": "ID is required for deletion"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            ter = trainer.objects.get(id=trainer_id)
            ter.delete()
            return Response(
                {"message": "Data deleted successfully", "success": True},
                status=status.HTTP_200_OK,
            )
        except trainer.DoesNotExist:
            return Response(
                {"error": "trainer not found"}, status=status.HTTP_404_NOT_FOUND
            )

    return Response({"error": "Invalid request method"}, status=405)
