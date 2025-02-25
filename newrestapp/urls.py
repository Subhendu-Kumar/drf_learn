from django.urls import path, include
from newrestapp import views
from rest_framework.routers import DefaultRouter  # type: ignore

router = DefaultRouter()
router.register(r"waiter", views.waiterViewSet, basename="waiter")

urlpatterns = [
    path("", include(router.urls)),
]
