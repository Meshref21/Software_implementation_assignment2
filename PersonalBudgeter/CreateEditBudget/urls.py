from django.urls import path
from . import views

urlpatterns = [
    path("create-budget/", views.go_to_create_budget, name="create_budget"),
    path("edit-budget/<int:pk>/", views.edit_budget, name="edit_budget"),
    path("delete-budget/<int:pk>/", views.delete_budget, name="delete_budget"),
]