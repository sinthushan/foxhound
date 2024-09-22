from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from .models import Applicant, Links
from .serialiers import ApplicantSeralizer, LinkSeralizer
from rest_framework.decorators import api_view
from utils.gmail import authenticate, search_emails, SCOPES




class ApplicantDetail(APIView):

    def get(self, request, format=None):
        user = self.request.user
        serializer = ApplicantSeralizer(user)
        return Response(serializer.data)

@api_view()
def link_account(request):
    creds = None
    user = request.user
    print(user)
    link = Links.objects.filter(applicant=user)
    if link:
        creds = link[0].creds
        creds = Credentials.from_authorized_user_info(json.loads(creds), SCOPES)
        creds = authenticate(creds)
        serializer =  LinkSeralizer(user, data={'creds': creds.to_json()})
        if serializer.is_valid(): 
            serializer.save() 
    else:
        creds = authenticate(creds)
        serializer =  LinkSeralizer(data={'applicant': user.id, 'creds': creds.to_json()})
        if serializer.is_valid(): 
            serializer.save()
        print(serializer.errors)     
    service = build('gmail', 'v1', credentials=creds)
    rejections = search_emails(service,'"received your application" after:2024/09/01')
    return Response({'rejections':rejections})