import io
from rest_framework.parsers import JSONParser  # type: ignore
from rest_framework.renderers import JSONRenderer  # type: ignore
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from restapp2.serializer import teacher_serializer

# Create your views here.


@csrf_exempt
def create_teacher(request):
    if request.method == "POST":
        data = request.body
        stream = io.BytesIO(data)
        py_data = JSONParser().parse(stream)
        serializer = teacher_serializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            res = {"message": "data inserted successfully", "success": True}
            jsondata = JSONRenderer().render(res)
            return HttpResponse(jsondata, content_type="application/json", status=201)
        else:
            jsondata = JSONRenderer().render(serializer.errors)
            return HttpResponse(jsondata, content_type="application/json", status=400)
