from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from datetime import timedelta
from .models import Applicant, Links
from .serialiers import ApplicantSeralizer, LinkSeralizer
from rest_framework.decorators import api_view
from utils.gmail import authenticate, search_emails, SCOPES
from django.utils import timezone



class ApplicantDetail(APIView):

    def get(self, request, format=None):
        user = self.request.user
        serializer = ApplicantSeralizer(user)
        return Response(serializer.data)
    
    def put(self, request):
        user = self.request.user
        serializer = ApplicantSeralizer(user, data=request.data, partial=True)
        if serializer.is_valid(): 
            serializer.save() 

@api_view()
def link_account(request):
    creds = None
    user = request.user
    link = Links.objects.filter(applicant=user)
    if link:
        creds = link[0].creds
        last_check = link[0].last_check.date()  +  timedelta(days=-1)
        
        creds = Credentials.from_authorized_user_info(json.loads(creds), SCOPES)
        creds = authenticate(creds)
    
        serializer =  LinkSeralizer(link.first(), data={'creds': creds.to_json()}, partial=True)
        if serializer.is_valid(): 
            serializer.save() 
    else:
        creds = authenticate(creds)
        serializer =  LinkSeralizer(data={'applicant': user.id, 'creds': creds.to_json()})
        if serializer.is_valid():
            serializer.save()
    service = build('gmail', 'v1', credentials=creds)
    applications = search_emails(service,f'"your application" after:{last_check}')
    return Response({'applications':applications})