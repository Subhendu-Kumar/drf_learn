from django.contrib import admin
from restapp7 import models

# Register your models here.


@admin.register(models.tester)
class tester_admin(admin.ModelAdmin):
    list_display = ["name", "email", "salary", "age"]
