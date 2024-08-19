from rest_framework import generics
from .models import Job, Stage
from .serializers import JobSerializer, StageSeralizer

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class StageCreate(generics.CreateAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSeralizer