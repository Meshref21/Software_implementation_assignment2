from rest_framework import serializers
from .models import BlogPost
from addTransactions.models import Transaction

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published_date']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'isIncome', 'amount', 'category', 'paymentMethod', 'description', 'transactionDate']

