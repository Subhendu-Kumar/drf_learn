from rest_framework import serializers  # type: ignore
from restapp5 import models


class person_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.person
        fields = "__all__"
