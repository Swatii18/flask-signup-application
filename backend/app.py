from flask import Flask, request, jsonify
import json
from dotenv import load_dotenv
import os
import pymongo
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

db = client.test

collection = db['flask_app']
app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('username')
    form_data = dict(request.json)
    file_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(file_path, 'r') as f:
     data = json.load(f)
     new_record = {
    'username': form_data.get('username')
}

    data.append(new_record)
    with open(file_path, 'w') as f:
        json.dump(data, f)

    collection.insert_one(form_data)
    #form_data['_id'] = str(form_data['_id'])
    # username = request.form.get('username')

    return 'data submitted successfully'

@app.route('/View')
def View():
    data = collection.find()
    data = list(data)
    for item in data:
     print(item)
     del item['_id']

    # del item['Password']
    # form_data['_id'] = str(form_data['_id'])
    
    data = {
        'data': data
    }
    return jsonify(data)

@app.route('/api')
def api():
    
    #locate data.json file

    file_path = os.path.join(os.path.dirname(__file__), 'data.json')

    #load the contents of data.json and return it as a JSON response
    with open(file_path, 'r') as f:
     data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
 
  app.run(host='0.0.0.0', port=9000, debug=True)
