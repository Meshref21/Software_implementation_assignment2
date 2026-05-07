from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Budget
from django.contrib.auth.decorators import login_required


@login_required
def go_to_create_budget(request):
    if request.method == "POST":
        category = request.POST.get("category")
        amount = request.POST.get("amount")
        period = request.POST.get("period")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        Budget.objects.create(
            user=request.user,
            category=category,
            amount=amount,
            period=period,
            start_date=start_date,
            end_date=end_date,
            remaining_amount=amount
        )

        messages.success(request, "Budget saved successfully.")
        return redirect("create_budget")

    budgets = Budget.objects.filter(user=request.user)
    total_budget = sum(b.amount for b in budgets)
    total_remaining = sum(b.remaining_amount for b in budgets)

    return render(request, "Create_Budget.html", {
        "budgets": budgets,
        "total_budget": total_budget,
        "total_remaining": total_remaining,
    })


@login_required
def edit_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)

    if request.method == "POST":
        budget.category = request.POST.get("category")
        budget.amount = request.POST.get("amount")
        budget.period = request.POST.get("period")
        budget.start_date = request.POST.get("start_date")
        budget.end_date = request.POST.get("end_date")
        budget.remaining_amount = request.POST.get("remaining_amount")
        budget.save()

        messages.success(request, "Budget updated successfully.")
        return redirect("create_budget")

    return render(request, "Edit_Budget.html", {"budget": budget})


@login_required
def delete_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    budget.delete()
    messages.success(request, "Budget deleted successfully.")
    return redirect("create_budget")