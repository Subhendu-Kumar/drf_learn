from rest_framework import serializers  # type: ignore
from restapp import models


class stu_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    branch = serializers.CharField(max_length=5)
    marks = serializers.IntegerField()
    age = serializers.IntegerField()
    date_created = serializers.DateTimeField()
