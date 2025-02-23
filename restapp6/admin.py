from django.contrib import admin
from restapp6 import models

# Register your models here.


@admin.register(models.trainer)
class trainer_admin(admin.ModelAdmin):
    list_display = ["name", "email", "salary", "age"]
