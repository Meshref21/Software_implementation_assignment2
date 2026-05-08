from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budgets")

    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(
        max_length=20,
        choices=[
            ("weekly", "Weekly"),
            ("monthly", "Monthly"),
            ("yearly", "Yearly"),
        ],
        default="monthly"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.remaining_amount:
            self.remaining_amount = self.amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.amount} ({self.period})"