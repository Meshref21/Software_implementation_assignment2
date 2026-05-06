from django.urls import path
from . import views

urlpatterns = [
    path('', views.goal_list, name='goal_list'),
    path('add/', views.create_goal, name='create_goal'),
    path('<int:goal_id>/update/', views.update_goal_progress, name='update_goal_progress'),
    path('<int:goal_id>/delete/', views.delete_goal, name='delete_goal'),
]