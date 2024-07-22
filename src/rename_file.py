def rename_file_drive(file_id, service):
    new_name = f'processado_{file_id}'
    try:
        file_metadata = {
            'name': new_name
        }

        updated_file = service.files().update(
            fileId=file_id,
            body=file_metadata,
            fields='name'
        ).execute()

        print(f'Arquivo processado com sucesso')

    except Exception as e:
        print(f'Ocorreu um erro ao renomear o arquivo: {str(e)}')
