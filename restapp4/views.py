import io
from rest_framework.parsers import JSONParser  # type: ignore
from rest_framework.renderers import JSONRenderer  # type: ignore
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from restapp4.serializer import employee_serializer
from restapp4.models import employee
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.


@method_decorator(csrf_exempt, name="dispatch")
class emp_data(View):
    def get(self, request, *args, **kwargs):
        data = request.body
        if data:
            stream = io.BytesIO(data)
            py_data = JSONParser().parse(stream)
            employee_id = py_data.get("id", None)
            if employee_id is not None:
                try:
                    em = employee.objects.get(id=employee_id)
                    serial = employee_serializer(em)
                    return JsonResponse(serial.data, status=200)
                except employee.DoesNotExist:
                    return JsonResponse({"error": "employee not found"}, status=404)

        em = employee.objects.all()
        serial = employee_serializer(em, many=True)
        return JsonResponse(serial.data, safe=False, status=200)

    def post(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        py_data = JSONParser().parse(stream)
        serializer = employee_serializer(data=py_data)
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
        employee_id = py_data.get("id", None)
        if employee_id is None:
            return JsonResponse({"error": "ID is required for update"}, status=400)
        try:
            em = employee.objects.get(id=employee_id)
            serial = employee_serializer(em, data=py_data, partial=True)
            if serial.is_valid():
                serial.save()
                return JsonResponse(
                    {"message": "Data updated successfully", "success": True},
                    status=200,
                )
            return JsonResponse(serial.errors, status=400)
        except employee.DoesNotExist:
            return JsonResponse({"error": "employee not found"}, status=404)

    def delete(self, request, *args, **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        py_data = JSONParser().parse(stream)
        employee_id = py_data.get("id", None)
        if employee_id is None:
            return JsonResponse({"error": "ID is required for deletion"}, status=400)
        try:
            em = employee.objects.get(id=employee_id)
            em.delete()
            return JsonResponse(
                {"message": "Data deleted successfully", "success": True}, status=200
            )
        except employee.DoesNotExist:
            return JsonResponse({"error": "employee not found"}, status=404)
