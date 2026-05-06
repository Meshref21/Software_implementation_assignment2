# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login

# def login_view(request):
#     return render(request, "login.html")

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from ..Home.views import homePageView

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("home/", views.homePageView, name="home"),
]