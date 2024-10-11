from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os
import base64
from bs4 import BeautifulSoup
import en_core_web_trf

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate(creds = None):
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except:
                pass
        flow = InstalledAppFlow.from_client_secrets_file(
           'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

    return creds

def search_emails(service, query):
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])

    msg_list = []
    if  messages:  

        for message in messages:
            try:
                snippet = base64.urlsafe_b64decode(service.users().messages().get(userId='me', id=message['id']).execute()['payload']['body']['data'])
                headers = service.users().messages().get(userId='me', id=message['id']).execute()['payload']['headers']
                
                for header in headers:
                    if header['name'] == 'From':
                        email_from = header['value'].split("@")[1].split('.')[-2]
               
                soup = BeautifulSoup(snippet, 'html.parser').get_text()
                print("yo")
                print(email_from)
                nlp = en_core_web_trf.load()
               
                doc = nlp(soup)

                company = [x.text for x in doc.ents if x.label_ == "ORG"]
                if company:
                    msg_list.append(company)
                elif email_from:
                    msg_list.append(email_from)
            except:
                pass

    return msg_list