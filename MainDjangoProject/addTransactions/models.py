from django.db import models

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

    isIncome = models.BooleanField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=categoryChoices)
    paymentMethod = models.CharField(max_length=50, choices=paymentChoices)
    description = models.CharField(max_length=200)
    

    