from django.contrib import admin
from newrestapp2 import models

# Register your models here.


@admin.register(models.dancer)
class dancer_admin(admin.ModelAdmin):
    list_display = ["name", "email", "salary", "age"]
