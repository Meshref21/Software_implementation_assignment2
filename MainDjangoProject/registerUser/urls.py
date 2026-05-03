from django.urls import path
from . import views

urlpatterns = [
    path('', views.addRegisterPage, name='add_register_page'),
]