from django.urls import  path
from . import views 

urlpatterns = [
    path('CreataBudget/', views.go_to_CreatBudget, name='Budget Creation'),
]
