from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os
import base64
from bs4 import BeautifulSoup
import en_core_web_trf

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate(creds = None):
    # if os.path.exists('token.pickle'):
    #     with open('token.pickle', 'rb') as token:
    #         creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        # with open('token.pickle', 'wb') as token:
        #     pickle.dump(creds, token)
    return creds

def search_emails(service, query):
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])
    msg_list = []
    if  messages:  

        for message in messages:
            try:
                snippet = base64.urlsafe_b64decode(service.users().messages().get(userId='me', id=message['id']).execute()['payload']['body']['data'])
                soup = BeautifulSoup(snippet, 'html.parser').get_text()
                nlp = en_core_web_trf.load()
               
                doc = nlp(soup)

                company = [x.text for x in doc.ents if x.label_ == "ORG"]
                msg_list.append(company)
            except:
                pass

    return msg_list