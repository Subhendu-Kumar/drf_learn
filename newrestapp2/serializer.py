from rest_framework import serializers  # type: ignore
from newrestapp2 import models


class dancer_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.dancer
        fields = "__all__"
