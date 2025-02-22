from django.contrib import admin
from restapp2.models import teacher

# Register your models here.


@admin.register(teacher)
class teacher_admin(admin.ModelAdmin):
    list_display = ["name", "email", "salary", "age"]
