from rest_framework import serializers  # type: ignore
from restapp2.models import teacher


class teacher_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    salary = serializers.IntegerField()
    age = serializers.IntegerField()

    def create(self, validated_data):
        return teacher.objects.create(**validated_data)