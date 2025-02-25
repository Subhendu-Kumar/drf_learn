from django.db import models

# Create your models here.


class singer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    salary = models.IntegerField()
    age = models.IntegerField()

    class Meta:
        db_table = "singer"
