from django.urls import path, include
from rest_framework.routers import DefaultRouter  # type: ignore
from restapp9.views import tester_view  # Make sure this is your correct view

router = DefaultRouter()
router.register(r"test", tester_view)

urlpatterns = [
    path("", include(router.urls)),  # Includes all registered ViewSet routes
]
