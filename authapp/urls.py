from django.urls import path
from authapp import views

urlpatterns = [
    path("register/", views.UserRegistrationView.as_view()),
    path("login/", views.UserLoginView.as_view()),
    path("profile/", views.profile.as_view()),
]
