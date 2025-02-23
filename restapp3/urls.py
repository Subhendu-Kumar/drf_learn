from django.urls import path
from restapp3 import views

urlpatterns = [path("", views.update_teacher)]
