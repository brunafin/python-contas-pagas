import schedule
import time
from datetime import datetime
from src import get_file, read_file
from flask import Flask, request, jsonify, make_response
from src.google_drive import google_drive_authentication
import pandas as pd
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Bem-vindo ao serviço comprovantes de Contas Pagas!"

@app.route('/upgrade-files', methods=['GET'])
def upgrade_payment_files():
    service = google_drive_authentication.authenticate()
    get_file.donwload_files(service)
    return jsonify('Arquivos atualizados')

@app.route('/get-files', methods=['GET'])
def get_files_list():
    resultDf = read_file.read_csv('src/files/banco.csv')
    resultDf['data'] = pd.to_datetime(resultDf['data'], format='%d/%m/%Y')
    resultDf = resultDf.sort_values(by='data', ascending=False)

    json_data = resultDf.to_json(orient='records', date_format='iso')
    json_data = json.loads(json_data)

    return make_response(jsonify(json_data), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030)
