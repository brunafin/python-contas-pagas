import pandas as pd
import os

def write_csv(content):
  header = ['id', 'tipo', 'valor', 'recebedor', 'data']
  dados = {}
  for index, item in enumerate(content.split(';')):
    if item:
      dados[header[index]] = [item]
  df = pd.DataFrame(dados)

  csv_file = 'src/files/banco.csv'
  if os.path.exists(csv_file):
    df.to_csv(csv_file, mode='a', header=False, index=False, sep=';')
  else:
    df.to_csv(csv_file, mode='w', header=True, index=False, sep=';', )
