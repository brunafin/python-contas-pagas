import os

def delete_file():
  path = 'src/files/comprovante.pdf'
  if os.path.exists(path):
    os.remove(path)
  else:
    print('Arquivo não encontrado')

# def delete_from_drive(file_id, service):
#   try:
#       # Deletar o arquivo
#       service.files().delete(fileId=file_id).execute()
#       print(f'Arquivo com ID {file_id} foi deletado com sucesso do Google Drive.')
#   except Exception as e:
#       print(f'Ocorreu um erro ao deletar o arquivo: {e}')

