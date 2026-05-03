from rest_framework import serializers
from .models import BlogPost
from addTransactions.models import Transaction
from registerUser.models import RegisterUser
from CreateEditBudget.models import Budget

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published_date']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'isIncome', 'amount', 'category', 'paymentMethod', 'description', 'transactionDate']

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['id', 'name', 'email', 'password']
    
class CreateEditBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'category', 'amount', 'period', 'start_date', 'end_date', 'remaining_amount', 'created_at', 'updated_at']