from flask import Flask, request, url_for
from flask_pymongo import PyMongo 

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/vogohelmetsdata'
mongo = PyMongo(app)

@app.route('/mongo', methods=['GET'])
def get_all_docs(data):
  doc = mongo.db.totalhelmetdata.insert({'abcd':'abcd'})
  return "inserted"