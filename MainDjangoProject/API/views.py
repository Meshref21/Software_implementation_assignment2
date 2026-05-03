from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer, TransactionSerializer, RegisterUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from addTransactions.models import Transaction
from registerUser.models import RegisterUser

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class RegisterUserListCreate(generics.ListCreateAPIView):
    queryset = RegisterUser.objects.all()
    serializer_class = RegisterUserSerializer