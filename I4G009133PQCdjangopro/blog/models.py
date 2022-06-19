from turtle import title
from typing_extensions import Self
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

user = settings.AUTH_USER_MODEL

user = get_user_model()

# Create your models here.
class post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(max_length=400)
    Author = models.ForeignKey(user, on_delete=models.CASCADE)
    Created_date =  models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)

