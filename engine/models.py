from django.db import models
from django.contrib.auth.forms import User


class MyUser(User):
    secret_key = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11, blank=True)