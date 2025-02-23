import io
from rest_framework.parsers import JSONParser  # type: ignore
from rest_framework.renderers import JSONRenderer  # type: ignore
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from restapp5.serializer import person_serializer
from restapp5.models import person
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.


@method_decorator(csrf_exempt, name="dispatch")
class per_data(View):
    def get(self, request, *args, **kwargs):
        data = request.body
        if data:
            stream = io.BytesIO(data)
            py_data = JSONParser().parse(stream)
            person_id = py_data.get("id", None)
            if person_id is not None:
                try:
                    per = person.objects.get(id=person_id)
                    serial = person_serializer(per)
                    return JsonResponse(serial.data, status=200)
                except person.DoesNotExist:
                    return JsonResponse({"error": "person not found"}, status=404)

        per = person.objects.all()
        serial = person_serializer(per, many=True)
        return JsonResponse(serial.data, safe=False, status=200)

    def post(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        py_data = JSONParser().parse(stream)
        serializer = person_serializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"message": "Data inserted successfully", "success": True}, status=201
            )
        return JsonResponse(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        py_data = JSONParser().parse(stream)
        person_id = py_data.get("id", None)
        if person_id is None:
            return JsonResponse({"error": "ID is required for update"}, status=400)
        try:
            per = person.objects.get(id=person_id)
            serial = person_serializer(per, data=py_data, partial=True)
            if serial.is_valid():
                serial.save()
                return JsonResponse(
                    {"message": "Data updated successfully", "success": True},
                    status=200,
                )
            return JsonResponse(serial.errors, status=400)
        except person.DoesNotExist:
            return JsonResponse({"error": "person not found"}, status=404)

    def delete(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        py_data = JSONParser().parse(stream)
        person_id = py_data.get("id", None)
        if person_id is None:
            return JsonResponse({"error": "ID is required for deletion"}, status=400)
        try:
            per = person.objects.get(id=person_id)
            per.delete()
            return JsonResponse(
                {"message": "Data deleted successfully", "success": True}, status=200
            )
        except person.DoesNotExist:
            return JsonResponse({"error": "person not found"}, status=404)
