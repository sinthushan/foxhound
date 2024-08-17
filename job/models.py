from django.db import models
from user.models import Profile
from django.utils.translation import gettext_lazy

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    applied_date = models.DateField(auto_now_add=True)
    modefied_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} at {self.company}'
    

class Stage(models.Model):
    class ApplicationStatus(models.TextChoices):
        APPLIED = "AP", gettext_lazy("Applied")
        INTERVIEW = "IN", gettext_lazy("Interview")
        REJECTED = "RE", gettext_lazy("Rejected")
        OFFER = "OF", gettext_lazy("Offer")
    
    stage = models.CharField(max_length=2, choices=ApplicationStatus.choices, default=ApplicationStatus.APPLIED)
    round = models.IntegerField(blank=True)
    comment = models.TextField(max_length=500)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='stages')