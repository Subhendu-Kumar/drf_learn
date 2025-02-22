from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from restapp.serializer import student_serializer
from restapp import models

# Create your views here.


class student_details(APIView):
    def get(self, request):
        stu = models.student.objects.all()
        stu_serializer = student_serializer(stu, many=True)
        return Response(stu_serializer.data)

    def post(self, request):
        pass
