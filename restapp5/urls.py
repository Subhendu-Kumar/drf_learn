from django.urls import path
from restapp5 import views

urlpatterns = [path("", views.per_data.as_view())]
