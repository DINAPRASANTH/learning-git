from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    clubname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.user.username
