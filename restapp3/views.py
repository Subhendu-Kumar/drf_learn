import io
from rest_framework.parsers import JSONParser  # type: ignore
from rest_framework.renderers import JSONRenderer  # type: ignore
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from restapp3.serializer import teacher_serializer
from restapp3.models import teacher

# Create your views here.


@csrf_exempt
def update_teacher(request):
    if request.method == "POST":
        data = request.body
        stream = io.BytesIO(data)
        py_data = JSONParser().parse(stream)
        serializer = teacher_serializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"message": "Data inserted successfully", "success": True}, status=201
            )
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "GET":
        data = request.body
        if data:
            stream = io.BytesIO(data)
            py_data = JSONParser().parse(stream)
            teacher_id = py_data.get("id", None)
            if teacher_id is not None:
                try:
                    tea = teacher.objects.get(id=teacher_id)
                    serial = teacher_serializer(tea)
                    return JsonResponse(serial.data, status=200)
                except teacher.DoesNotExist:
                    return JsonResponse({"error": "Teacher not found"}, status=404)

        tea = teacher.objects.all()
        serial = teacher_serializer(tea, many=True)
        return JsonResponse(serial.data, safe=False, status=200)

    elif request.method == "PUT":
        data = request.body
        stream = io.BytesIO(data)
        py_data = JSONParser().parse(stream)
        teacher_id = py_data.get("id", None)
        if teacher_id is None:
            return JsonResponse({"error": "ID is required for update"}, status=400)
        try:
            tea = teacher.objects.get(id=teacher_id)
            serial = teacher_serializer(tea, data=py_data, partial=True)
            if serial.is_valid():
                serial.save()
                return JsonResponse(
                    {"message": "Data updated successfully", "success": True},
                    status=200,
                )
            return JsonResponse(serial.errors, status=400)
        except teacher.DoesNotExist:
            return JsonResponse({"error": "Teacher not found"}, status=404)

    elif request.method == "DELETE":
        data = request.body
        stream = io.BytesIO(data)
        py_data = JSONParser().parse(stream)
        teacher_id = py_data.get("id", None)
        if teacher_id is None:
            return JsonResponse({"error": "ID is required for deletion"}, status=400)
        try:
            tea = teacher.objects.get(id=teacher_id)
            tea.delete()
            return JsonResponse(
                {"message": "Data deleted successfully", "success": True}, status=200
            )
        except teacher.DoesNotExist:
            return JsonResponse({"error": "Teacher not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=405)
