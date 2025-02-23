from django.contrib import admin
from restapp5 import models

# Register your models here.


@admin.register(models.person)
class person_admin(admin.ModelAdmin):
    list_display = ["name", "email", "age"]
