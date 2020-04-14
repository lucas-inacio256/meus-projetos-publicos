###############################################################################

## author: Lucas santos
## version: 1.0
## Python 3.6.5 | UTF-8

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

from datetime import date
from os import walk
from os import remove
import zipfile

###############################################################################

def get_datetime():
    return '-'.join( str(date.today()).split('-')[::-1] )

###############################################################################

def zipFolder(folder_path, zip_file_path):
    zip_file = zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in walk(folder_path):
        for file in files:
            zip_file.write( os.path.join(root, file) )

    zip_file.close()

###############################################################################

# Google Drive API Tutorial:
# https://developers.google.com/drive/api/v3/quickstart/python

def authBuild(SCOPES, PATH=''):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """

    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists(PATH + 'token.pickle'):
        with open(PATH + 'token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                PATH + 'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(PATH + 'token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)

###############################################################################

# Mime Types:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types

def uploadFile(drive_service, file_name, file_path, mime):
    file_metadata = {'name': file_name}

    media = MediaFileUpload(file_path, mime)

    file = drive_service.files().create(body = file_metadata,
                                        media_body = media,
                                        fields = 'id').execute()

    return file.get('id')
