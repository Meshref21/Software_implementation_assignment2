from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Register_View, name='register'),
]