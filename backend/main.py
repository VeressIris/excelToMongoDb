from flask import Flask, request
from flask_cors import CORS, cross_origin
import pandas as pd
import json
from pymongo import MongoClient
from urllib.parse import unquote

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def home():
    return "Server running"

@app.route('/convert', methods=['POST'])
def convert():
    df = pd.DataFrame()

    if 'file' not in request.files:
        google_sheets_link = request.form.get('sheets-link')
        if google_sheets_link:
            google_sheets_link = google_sheets_link.split('/edit')[0]
            try:
                df = pd.read_csv(f'{google_sheets_link}/export?format=csv')
            except Exception as e:
                return json.dumps({'success': False, 'message': 'Failed to read Google Sheets data'}), 400
        else:
            return json.dumps({'success': False, 'message': 'No file or Google Sheets link provided'}), 400
    else:
        df = pd.read_excel(request.files['file'])

    mongodb_link = request.form.get('mongodb-link')
    if not mongodb_link:
        return json.dumps({'success': False, 'message': 'No MongoDB link provided'}), 400
    
    collection = request.form.get('collection')
    if not collection:
        return json.dumps({'success': False, 'message': 'No MongoDB collection provided'}), 400
    
    db_name = request.form.get('db-name')
    if not db_name:
        return json.dumps({'success': False, 'message': 'No database name provided'}), 400

    objects = get_objects(df)
    
    client = MongoClient(unquote(mongodb_link))
    db = client[db_name]
    db[collection].insert_many(objects)

    return json.dumps({'success': True}), 200

def get_objects(df):
    cols = df.columns
    df = df.reset_index()
    objects = []
    for index, row in df.iterrows():
        obj = {}
        for col in cols:
            obj[col] = row[col]
        objects.append(obj)
    return objects

if __name__ == '__main__':
    app.run(debug=True)
