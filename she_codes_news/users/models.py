from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(("first name"), max_length=150, blank=True)
    last_name = models.CharField(("last name"), max_length=150, blank=True)
    birth_date = models.DateField(null=True)
    profile_photo = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, max_length=200)

    def __str__(self):
        return self.username
    


