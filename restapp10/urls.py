from django.urls import path, include
from rest_framework.routers import DefaultRouter  # type: ignore
from restapp9.views import tester_view  # Make sure this is your correct view

router = DefaultRouter()
router.register(r"tests", tester_view)

urlpatterns = [
    path("", include(router.urls)),  # Includes all registered ViewSet routes
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
