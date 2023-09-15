from __future__ import print_function
import json
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://mail.google.com/']

def get_credentials():
    """Get Google API credentials using OAuth 2.0 flow."""
    creds = None

    try:
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

    except Exception as e:
        print(f"Error loading credentials: {e}")
        print(creds)

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

service = create_service()