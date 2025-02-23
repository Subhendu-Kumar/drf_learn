from django.contrib import admin
from restapp4.models import employee

# Register your models here.


@admin.register(employee)
class employee_admin(admin.ModelAdmin):
    list_display = ["name", "email", "salary", "age"]
