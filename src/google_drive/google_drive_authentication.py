from google.oauth2 import service_account
from googleapiclient.discovery import build

def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'src/google_drive/credentials.json'

    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('drive', 'v3', credentials=credentials)
    return service
