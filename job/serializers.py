from rest_framework import serializers
from .models import Job, Stage

class StageSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields =  '__all__'

class JobSerializer(serializers.ModelSerializer):
    stages = StageSeralizer(many=True, read_only=True)
    class Meta:
        model = Job
        fields = [
            'id',
            'applicant', 
            'title',
            'company',
            'applied_date', 
            'modefied_date',
            'stages'
           
        ]
        read_only_fields = [
            'id',
            'applicant', 
            'applied_date', 
            'modefied_date',
            'stages'
        ]
    def create(self, validated_data):
        user =  self.context['request'].user
        job = Job.objects.create(applicant=user,**validated_data)
        Stage.objects.create(comment = f"Applied for {job.title} at {job.company}", round = 0, job=job)
        return job