from django.urls import path, include
from newrestapp2 import views
from rest_framework.routers import DefaultRouter  # type: ignore
from rest_framework.authtoken.views import obtain_auth_token  # type: ignore

router = DefaultRouter()
router.register(r"dancer", views.dancer_view, basename="dancer")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("gettoken/", obtain_auth_token),
]
