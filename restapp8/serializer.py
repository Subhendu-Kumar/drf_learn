from rest_framework import serializers  # type: ignore
from restapp8 import models


class tester_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.tester
        fields = "__all__"
