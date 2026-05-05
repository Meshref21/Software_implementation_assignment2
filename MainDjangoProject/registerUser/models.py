from django.db import models

class RegisterUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=50)