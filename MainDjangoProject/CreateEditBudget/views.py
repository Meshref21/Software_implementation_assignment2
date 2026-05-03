from django.shortcuts import render, redirect
from .models import Budget

# def go_to_create_budget(request):
#     if request.method == "POST":
#         category = request.POST.get("category")
#         amount = request.POST.get("amount")
#         period = request.POST.get("period")
#         start_date = request.POST.get("start_date")
#         end_date = request.POST.get("end_date")

#         Budget.objects.create(
#             category=category,
#             amount=amount,
#             period=period,
#             start_date=start_date,
#             end_date=end_date,
#             remaining_amount=amount
#         )

#         # return redirect("Create_Budget")

#     budgets = Budget.objects.all()

#     return render(request, "Create_Budget.html", {
#         "budgets": budgets
#     })

def go_to_create_budget(request):
    return render(request, "Create_Budget.html")