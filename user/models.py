from django.db import models
from django.contrib.auth.models import AbstractUser


class Applicant(AbstractUser):
   
    avatar = models.ImageField(blank=True)
    bio = models.TextField(max_length=500)
    def __str__(self) -> str:
        return self.username
