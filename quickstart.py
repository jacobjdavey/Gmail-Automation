from __future__ import print_function
import json
import os
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()

SCOPES = ['https://mail.google.com/']

def get_credentials():
    """Get Google API credentials."""
    creds = None
    credentials_json = os.getenv("CREDENTIALS_JSON")

    if credentials_json:
        creds = Credentials.from_authorized_user_info(json.loads(credentials_json), SCOPES)
    else:
        print("Error: Credentials JSON not found in environment variable.")
    return creds

def create_service():
    """Create Gmail API service."""
    creds = get_credentials()

    if not creds:
        return None

    try:
        service = build('gmail', 'v1', credentials=creds)
        return service

    except HttpError as error:
        print(f'An error occurred: {error}')
        return None
