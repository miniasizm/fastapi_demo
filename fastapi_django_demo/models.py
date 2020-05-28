from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    api_key = models.CharField(max_length=100, db_index=True)


class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    due = models.DateField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
