from rest_framework import serializers
from .models import BlogPost
from addTransactions.models import Transaction
from registerUser.models import RegisterUser

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
        fields = ['name', 'email', 'password']