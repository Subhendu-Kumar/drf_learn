from django.urls import path
from restapp8 import views

urlpatterns = [
    path("list_tester", views.tester_list.as_view()),
    path("create_tester", views.tester_crerate.as_view()),
    path("retrieve_tester/<int:pk>", views.tester_retrieve.as_view()),
    path("update_tester/<int:pk>", views.tester_update.as_view()),
    path("delete_tester/<int:pk>", views.tester_delete.as_view()),
    path("list_create_tester", views.tester_list_create.as_view()),
    path("retrieve_update_tester/<int:pk>", views.tester_retrieve_update.as_view()),
    path("retrieve_delete_tester/<int:pk>", views.tester_retrieve_delete.as_view()),
    path(
        "retrieve_update_delete_tester/<int:pk>",
        views.tester_retrieve_update_delete.as_view(),
    ),
]
