from rest_framework import serializers  # type: ignore
from restapp3.models import teacher


class teacher_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    salary = serializers.IntegerField()
    age = serializers.IntegerField()

    def create(self, validated_data):
        return teacher.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get("name", instance.name)
        instance.email = validate_data.get("email", instance.email)
        instance.salary = validate_data.get("salary", instance.salary)
        instance.age = validate_data.get("age", instance.age)
        instance.save()
        return instance
