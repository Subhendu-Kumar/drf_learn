from rest_framework import serializers  # type: ignore
from newrestapp1 import models


class singer_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.singer
        fields = "__all__"
