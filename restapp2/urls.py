from django.urls import path
from restapp2 import views

urlpatterns = [path("", views.create_teacher)]
