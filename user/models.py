from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Applicant(AbstractUser):
   
    avatar = models.ImageField(blank=True)
    bio = models.TextField(max_length=500)
    def __str__(self) -> str:
        return self.username

class Links(models.Model):
    applicant =  models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='links')
    creds = models.JSONField()
    last_check = models.DateTimeField(auto_now=True)      