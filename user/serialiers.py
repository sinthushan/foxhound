from rest_framework import serializers
from .models import Applicant, Links



class LinkSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = [
            'id',
            'applicant', 
            'creds',
        ]


class LinkUserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['id']

class ApplicantSeralizer(serializers.ModelSerializer):
    links = LinkUserSeralizer(many=True, read_only=True)
    class Meta:
        model = Applicant
        fields = ["email","username","first_name","last_name","avatar","bio", "pk","links"]
        read_only_fields = ["links"]