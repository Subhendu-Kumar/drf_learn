from django.contrib import admin
from newrestapp1 import models

# Register your models here.


@admin.register(models.singer)
class singer_admin(admin.ModelAdmin):
    list_display = ["name", "email", "salary", "age"]
