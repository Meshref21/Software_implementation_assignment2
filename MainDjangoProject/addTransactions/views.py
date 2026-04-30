from django.shortcuts import render

def addTransactionPage(request):
    return render(request, "addTransactions.html")
