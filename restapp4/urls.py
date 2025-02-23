from django.urls import path
from restapp4 import views

urlpatterns = [path("", views.emp_data.as_view())]
