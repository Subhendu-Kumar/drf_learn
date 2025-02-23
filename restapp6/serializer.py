from rest_framework import serializers  # type: ignore
from restapp6 import models


class trainer_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.trainer
        fields = "__all__"
