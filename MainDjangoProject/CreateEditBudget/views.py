from django.shortcuts import render, redirect
from .models import Budget


def go_to_create_budget(request):
    if request.method == "POST":
        category = request.POST.get("category")
        amount = request.POST.get("amount")
        period = request.POST.get("period")

        Budget.objects.create(
            category=category,
            amount=amount,
            period=period,
            remaining_amount=amount
        )

        return redirect("create_budget")

    budgets = Budget.objects.all()

    return render(request, "create_budget.html", {
        "budgets": budgets
    })