from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    secret_key = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11, blank=True)
    
