from django.db import model
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = model.models.CharField(max_length=50)
