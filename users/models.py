from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(unique=True)

    def __str__(self):
        return f'{self.username} - {self.email}'

# Create your models here.
