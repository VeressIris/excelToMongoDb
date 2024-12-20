from flask import Flask, request
from flask_cors import CORS, cross_origin
import pandas as pd
import json
from pymongo import MongoClient

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def home():
    return "Server running"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    mongodb_link = request.form.get('mongodb-link')
    if not mongodb_link:
        return 'No MongoDB link provided', 400
    
    collection = request.form.get('collection')
    if not collection:
        return 'No MongoDB collection provided', 400
    
    db_name = request.form.get('db-name')
    if not db_name:
        return 'No database provided', 400

    df = pd.read_excel(file)
    
    cols = df.columns
    df = df.reset_index()
    objects = []
    for index, row in df.iterrows():
        obj = {}
        for col in cols:
            obj[col] = row[col]
        objects.append(obj)
    
    client = MongoClient(mongodb_link)
    db = client[db_name]
    db[collection].insert_many(objects)

    return json.dumps({'success': True}), 200

@app.route('/convertSheets', methods=['POST'])
def convertSheets():
    google_sheets_link = request.form.get('sheets-link')
    if not google_sheets_link:
        return 'No Google Sheets link provided', 400

    mongodb_link = request.form.get('mongodb-link')
    if not mongodb_link:
        return 'No MongoDB link provided', 400
    
    collection = request.form.get('collection')
    if not collection:
        return 'No MongoDB collection provided', 400
    
    db_name = request.form.get('db-name')
    if not db_name:
        return 'No database provided', 400

    google_sheets_link = google_sheets_link[:google_sheets_link.find('/edit')]
    df = pd.read_csv(f'{google_sheets_link}/export?format=csv')

    cols = df.columns
    df = df.reset_index()
    objects = []
    for index, row in df.iterrows():
        obj = {}
        for col in cols:
            obj[col] = row[col]
        objects.append(obj)
    
    client = MongoClient(mongodb_link)
    db = client[db_name]
    db[collection].insert_many(objects)

    return json.dumps({'success': True}), 200

if __name__ == '__main__':
    app.run(debug=True)