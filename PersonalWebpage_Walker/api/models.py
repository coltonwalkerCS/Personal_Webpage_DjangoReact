from django.db import models
import string
import random


def generate_unique_code():
    length = 8

    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=length))
        if User.objects.filter(user_code=code).count() == 0:
            break

    return code


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=15)
    user_code = models.CharField(max_length=8, unique=True)