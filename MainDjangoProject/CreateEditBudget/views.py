from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def go_to_CreatBudget(request):
    return render(request, 'Create Budget.html')