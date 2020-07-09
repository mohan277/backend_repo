from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)


class AccountFactory(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_joined = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
