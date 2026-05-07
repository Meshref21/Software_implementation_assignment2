from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    
    categoryChoices = [
        ("food", "Food"),
        ("transport", "Transport"),
        ("shopping", "Shopping"),
        ("salary", "Salary"),
        ("other", "Other"),
    ]

    paymentChoices = [
        ("credit_card", "Credit Card"),
        ("master_card", "Master Card"),
        ("visa", "Visa"),
        ("mobile_wallet", "Mobile Wallet"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isIncome = models.BooleanField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=categoryChoices)
    paymentMethod = models.CharField(max_length=50, choices=paymentChoices)
    description = models.CharField(max_length=200)
    transactionDate = models.DateTimeField(auto_now_add=True)

    