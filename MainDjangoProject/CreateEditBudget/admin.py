from django.contrib import admin
from .models import Budget
# Register your models here.

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "amount",
        "period",
        "start_date",
        "end_date",
        "remaining_amount",
        "created_at",
    )
    list_filter = ("period", "category", "start_date")
    search_fields = ("category",)
    ordering = ("-created_at",)