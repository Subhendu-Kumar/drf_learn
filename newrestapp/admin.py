from django.contrib import admin
from newrestapp import models

# Register your models here.


@admin.register(models.waiters)
class waiters_admin(admin.ModelAdmin):
    list_display = ["name", "email", "salary", "age"]
