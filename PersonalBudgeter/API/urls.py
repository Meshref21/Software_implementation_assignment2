from django.urls import path
from . import views
from registerUser.views import users_api


urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("transaction/", views.TransactionListCreate.as_view(), name="transaction-view-create"),
    path("userinformation/", views.RegisterUserListCreate.as_view(), name="transaction-view-create"),
    path("createeditbudget/", views.CreateEditBudgetListCreate.as_view(), name="create-edit-budget"),
    path('users/', users_api, name='users_api'),

]