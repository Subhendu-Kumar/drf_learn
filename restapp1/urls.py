from django.urls import path
from restapp1 import views

urlpatterns = [
    path("stu/<int:pk>", views.std_details),
    path("stu/", views.std_all_details),
]
