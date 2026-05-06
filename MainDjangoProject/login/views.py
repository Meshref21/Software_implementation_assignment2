from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Here you would typically authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/goals/')  # Redirect to a home page or dashboard after successful login
        else:   
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })
        
        
    return render(request, 'login.html')


