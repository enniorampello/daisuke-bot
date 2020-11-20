from __future__ import print_function
from date_format import tomorrow, duration
import pickle
import os.path
import globals
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

class Calendar:

    def __init__(self) -> None:
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        
        self.service = build('calendar', 'v3', credentials=creds)

    def check(self):
        events_result = self.service.events().list(calendarId='primary', timeMin=tomorrow(),
                                        timeMax=tomorrow(add_days=1), singleEvents=True,
                                        orderBy='startTime').execute()
        events = events_result.get('items', [])

        for event in events:
            if event['summary'] in globals.material_urls.keys():
                globals.lectures.append((event['summary'],duration(event),event['colorId']))

    def run():
        pass

if __name__ == '__main__':
    calendar = Calendar()
    calendar.check()