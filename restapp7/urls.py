from django.urls import path, include
from restapp7 import views
from rest_framework.routers import DefaultRouter  # type: ignore

# Using DefaultRouter to generate URLs automatically
router = DefaultRouter()
router.register(r"testers", views.TesterViewSet)  # Endpoint: /testers/

urlpatterns = [
    path("", include(router.urls)),
    path("list", views.tester_list.as_view()),
    path("create", views.tester_create.as_view()),
    path("retrieve/<int:pk>", views.tester_retrieve.as_view()),
    path("update/<int:pk>", views.tester_update.as_view()),
    path("delete/<int:pk>", views.tester_delete.as_view()),
    path("tester1", views.tester1.as_view()),
    path("tester2/<int:pk>", views.tester2.as_view()),
]
