from rest_framework import serializers
from .models import Applicant

class ApplicantSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ["username","first_name","last_name","avatar","bio"]