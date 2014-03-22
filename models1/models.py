from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_password = models.CharField(max_length=30)
    user_email = models.EmailField()