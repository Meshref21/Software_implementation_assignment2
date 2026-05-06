from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def progress_percentage(self):
        if self.target_amount == 0:
            return 0

        progress = (self.current_amount / self.target_amount) * 100
        return min(round(progress, 2), 100)

    def is_completed(self):
        return self.current_amount >= self.target_amount

    def __str__(self):
        return f"{self.name} - {self.user.username}"