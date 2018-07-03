from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	'''
	To be completed
	'''
	phone = models.CharField("Phone", max_length=15, null=True, blank=True)