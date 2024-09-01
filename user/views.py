from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Applicant
from .serialiers import ApplicantSeralizer

class ApplicantDetail(APIView):

    def get(self, request, format=None):
        user = self.request.user
        serializer = ApplicantSeralizer(user)
        return Response(serializer.data)
