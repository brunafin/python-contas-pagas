import read_file
import write_file
import remove_file
import rename_file

def process_file(file_id, service):
  content = read_file.read_pdf('src/files/comprovante.pdf')
  write_file.write_csv(content)
  remove_file.delete_file()
  rename_file.rename_file_drive(file_id, service)
  return True
