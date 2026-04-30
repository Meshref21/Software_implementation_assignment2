from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("transaction/", views.TransactionListCreate.as_view(), name="transaction-view-create"),
]