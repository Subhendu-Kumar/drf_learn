from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    branch = models.CharField(max_length=5)
    marks = models.IntegerField()
    age = models.IntegerField()
    date_created = models.DateTimeField()
