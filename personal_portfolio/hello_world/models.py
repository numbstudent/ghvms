from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class UserUniqueToken(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    datetime = models.DateField(default=timezone.now)  # for token expiration
