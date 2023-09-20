from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CloudLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User model from Django auth
    account_id = models.CharField(max_length=255)
    access_key = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255)
