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
            'title',
            'company',
            'applicant', 
            'applied_date', 
            'modefied_date',
            'stages'
           
        ]
        read_only_fields = [
            'id',
            'applied_date', 
            'modefied_date',
            'stages'
        ]
    def create(self, validated_data):
        job = Job.objects.create(**validated_data)
        Stage.objects.create(comment = f"Applied for {job.title} at {job.company}", round = 0, job=job)
        return job