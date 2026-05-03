from django.shortcuts import render

def addRegisterPage(request):
    return render(request, "register.html")
