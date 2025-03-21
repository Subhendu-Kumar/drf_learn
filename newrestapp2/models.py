from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token  # type: ignore

# Create your models here.


class dancer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    salary = models.IntegerField()
    age = models.IntegerField()

    class Meta:
        db_table = "dancer"

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
