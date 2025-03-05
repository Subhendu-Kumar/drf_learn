from django.urls import path
from authapp import views

urlpatterns = [
    path("register/", views.user_registration_view.as_view()),
    path("login/", views.user_login_view.as_view()),
]
