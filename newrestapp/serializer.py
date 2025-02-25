from rest_framework import serializers  # type: ignore
from newrestapp import models


class waiters_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.waiters
        fields = "__all__"
