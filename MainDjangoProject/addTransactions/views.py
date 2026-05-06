from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required

def addTransactionPage(request):
    return render(request, "addTransactions.html")
