import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/calendar"]
dirname = os.path.dirname(__file__)
CREDENTIALS_FILE = os.path.join(dirname,"credentials.json")
TOKENS_FILE = os.path.join(dirname,"token.pickle")


def get_calendar_service():
    creds = None

    if os.path.exists(TOKENS_FILE):
        with open(TOKENS_FILE, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=35665)
            
        with open(TOKENS_FILE, "wb") as token:
            pickle.dump(creds, token)
            
        with open('/home/google/task/token.json', 'w') as token:
            token.write(creds.to_json())
    service = build("calendar", "v3", credentials=creds)
    print(service)
    return service