from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
load_dotenv()

google_drive_folder_id = os.getenv('GOOGLE_DRIVE_FOLDER_ID')
credentials_type = os.getenv('GOOGLE_DRIVE_CREDENTIALS_TYPE')
credentials_project_id = os.getenv('GOOGLE_DRIVE_CREDENTIALS_PROJECT_ID')
credentials_private_key_id = os.getenv('GOOGLE_DRIVE_CREDENTIALS_PRIVATE_KEY_ID')
credentials_private_key = os.getenv('GOOGLE_DRIVE_CREDENTIALS_PRIVATE_KEY')
credentials_client_email = os.getenv('GOOGLE_DRIVE_CREDENTIALS_CLIENT_EMAIL')
credentials_client_id = os.getenv('GOOGLE_DRIVE_CREDENTIALS_CLIENT_ID')
credentials_auth_uri = os.getenv('GOOGLE_DRIVE_CREDENTIALS_AUTH_URI')
credentials_token_uri = os.getenv('GOOGLE_DRIVE_CREDENTIALS_TOKEN_URI')
credentials_auth_provider_x509_cert_url = os.getenv('GOOGLE_DRIVE_CREDENTIALS_AUTH_PROVIDER_X509_CERT_URL')
credentials_client_x509_cert_url = os.getenv('GOOGLE_DRIVE_CREDENTIALS_CLIENT_X509_CERT_URL')
credentials_universe_domain = os.getenv('GOOGLE_DRIVE_CREDENTIALS_UNIVERSE_DOMAIN')

credentials_obj = {
  "type": credentials_type,
  "project_id": credentials_project_id,
  "private_key_id": credentials_private_key_id,
  "private_key": credentials_private_key,
  "client_email": credentials_client_email,
  "client_id": credentials_client_id,
  "auth_uri": credentials_auth_uri,
  "token_uri": credentials_token_uri,
  "auth_provider_x509_cert_url": credentials_auth_provider_x509_cert_url,
  "client_x509_cert_url": credentials_client_x509_cert_url,
  "universe_domain": credentials_universe_domain
}

def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'src/google_drive/credentials.json'

    credentials = service_account.Credentials.from_service_account_info(credentials_obj, scopes=SCOPES)

    service = build('drive', 'v3', credentials=credentials)
    return service
