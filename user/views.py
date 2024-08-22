from rest_framework import generics
from .models import Applicant
from .serialiers import ApplicantSeralizer

class ApplicantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSeralizer
