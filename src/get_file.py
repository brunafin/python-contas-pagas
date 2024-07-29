from dotenv import load_dotenv
from googleapiclient.http import MediaIoBaseDownload
from src import process_file
import os
import io

load_dotenv()
google_drive_folder_id = os.getenv('GOOGLE_DRIVE_FOLDER_ID')

def donwload_files(service):
    query = f"'{google_drive_folder_id}' in parents and trashed=false and not name contains 'processado'"
    results = service.files().list(q=query, pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('Nenhum arquivo encontrado.')
        return False
    else:
        for item in items:
            file_id = item["id"]
            request = service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)

            done = False
            while not done:
                status, done = downloader.next_chunk()
            file_name = f'comprovante.pdf'
            file_path = os.path.join(os.getcwd(), 'src', 'files', file_name)

            with open(file_path, 'wb') as f:
                fh.seek(0)
                f.write(fh.read())

            process_file.process_file(file_id, service)
