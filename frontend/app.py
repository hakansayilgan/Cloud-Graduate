from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

@app.route('/')
def hello():


    client = MongoClient(f'mongodb://mongodb-service.default.svc.cluster.local:27017/?')
    db = client['task']
    names_collection = db['names']
    name = names_collection.find_one()['name']
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
