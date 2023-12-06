from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birth_date = models.DateTimeField(null=True)
    profile_photo = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, max_length=200)

    def __str__(self):
        return self.username
    