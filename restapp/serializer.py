from rest_framework import serializers  # type: ignore
from restapp import models


class student_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.student
        fields = "__all__"
