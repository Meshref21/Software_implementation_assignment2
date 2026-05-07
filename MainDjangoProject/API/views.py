from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer, TransactionSerializer, RegisterUserSerializer, CreateEditBudgetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from addTransactions.models import Transaction
from registerUser.models import RegisterUser
from CreateEditBudget.models import Budget

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class TransactionListCreate(generics.ListCreateAPIView):
    # queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegisterUserListCreate(generics.ListCreateAPIView):
    queryset = RegisterUser.objects.all()
    serializer_class = RegisterUserSerializer

class CreateEditBudgetListCreate(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = CreateEditBudgetSerializer