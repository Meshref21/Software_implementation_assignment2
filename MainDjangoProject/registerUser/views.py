from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # check passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'registerUser/register.html')

        # check username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return render(request, 'registerUser/register.html')

        # check email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, 'registerUser/register.html')

        # create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created! Please login.")
        return redirect('login')

    return render(request, 'registerUser/register.html')