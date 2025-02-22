from rest_framework.renderers import JSONRenderer  # type: ignore
from restapp1.serializer import stu_serializer
from django.http import HttpResponse
from restapp1 import models

# Create your views here.


def std_details(request, pk):
    std = models.student.objects.get(id=pk)
    serializer = stu_serializer(std)
    data = JSONRenderer().render(serializer.data)
    return HttpResponse(data, content_type="application/json")


def std_all_details(request):
    std = models.student.objects.all()
    serializer = stu_serializer(std, many=True)
    data = JSONRenderer().render(serializer.data)
    return HttpResponse(data, content_type="application/json")
