from django.contrib import admin
from authapp.models import User

# Register your models here.


@admin.register(User)
class user_admin(admin.ModelAdmin):
    list_display = ["name", "email", "tc", "is_active"]
