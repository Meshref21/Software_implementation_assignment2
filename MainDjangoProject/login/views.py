from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# def login_view(request):
#     return render(request, "login.html")

# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views
# from ..Home.views import homePageView

# urlpatterns = [
#     path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
#     path("logout/", auth_views.LogoutView.as_view(), name="logout"),
#     path("home/", views.homePageView, name="home"),
# ]

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next")


        print("USERNAME", username)
        print("Password", password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if next_url:
                return redirect(next_url)
            return redirect("/home")  # name of your home url

        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    print("Hello")
    return render(request, "login.html")