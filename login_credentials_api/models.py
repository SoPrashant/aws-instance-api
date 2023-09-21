from django.db import models
from cryptography.fernet import Fernet


# Create your models here.
class CloudLogin(models.Model):
    account_id = models.CharField(max_length=255)
    access_key = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255)
