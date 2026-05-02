from django.urls import path
from . import views

urlpatterns = [
    path("create-budget/", views.go_to_create_budget, name="create_budget"),
]