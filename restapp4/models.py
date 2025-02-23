from django.db import models

# Create your models here.


class employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    salary = models.IntegerField()
    age = models.IntegerField()
