from django.urls import path, include
from newrestapp1 import views
from rest_framework.routers import DefaultRouter  # type: ignore

router = DefaultRouter()
router.register(r"singer", views.singer_view, basename="signer")

urlpatterns = [
    path("", include(router.urls)),
]
