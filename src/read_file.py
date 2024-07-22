import pandas as pd
from PyPDF2 import PdfReader
import re

def read_csv(path_file):
  df = pd.read_csv(path_file, delimiter=';')
  return df

def read_pdf(path_file):
  padrao_data = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b'
  reader =  PdfReader(path_file)
  number_of_pages = len(reader.pages)
  data = []
  convertLine = ''
  header = reader.pages[0].extract_text().splitlines()[0]
  tipo_comprovante = ''
  if "água" in header:
    tipo_comprovante = "agua"
  elif "QR" in header:
    tipo_comprovante = 'QR'
  else:
    tipo_comprovante = "Pessoa"

  for index, item in enumerate(reader.pages):
    page = reader.pages[index]
    text = page.extract_text()
    lines = text.splitlines()

    for line in lines:
      if tipo_comprovante == 'Pessoa' or tipo_comprovante == 'QR':
        if "nome" in line or (tipo_comprovante == 'QR' and "valor: R$" in line) or (tipo_comprovante != 'QR' and 'R$' in line) or "realizado em" in line or "ID da transação" in line:
          data.append(line)
      if tipo_comprovante == 'agua':
        datas_encontradas = re.findall(padrao_data, line)
        if "0086-" in line or "R$" in line or "Autenticação" in line:
          data.append(line)
        if datas_encontradas:
          data.append(line)
  if tipo_comprovante == 'agua':
    convertedValueToFloat = float(data[1].split('R$')[1].strip().replace('.',',').replace(',','.'))
    convertToLine = f'''{data[-1].split('Autenticação ')[1].split(" ")[0]};Boleto;{convertedValueToFloat};{data[0].strip()};{data[2].split('às')[0].strip()};'''
  elif tipo_comprovante == 'QR':
    convertedValueToFloat = float(data[1].split('R$')[1].strip().replace('.',',').replace(',','.'))
    convertToLine = f'''{data[-1].split('ID da transação: ')[1]};Pix;{convertedValueToFloat};{data[2].split('Favorecido: ')[1]};{data[3].split('realizado em ')[1].split(' ')[0]};'''
  elif tipo_comprovante == 'Pessoa':
    convertedValueToFloat = float(data[0].split('R$')[1].strip().replace('.',',').replace(',','.'))
    convertToLine = f'''{data[-1].split('ID da transação: ')[1]};Pix;{convertedValueToFloat};{data[2].split('nome do favorecido ')[1]};{data[3].split(',')[0].split('realizado em ')[1]};'''
  else:
    print('Outro')
  return convertToLine


