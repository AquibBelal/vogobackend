from flask import Flask, request, url_for, jsonify
from flask_pymongo import PyMongo 

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/vogohelmetsdata'
mongo = PyMongo(app)

@app.route('/mongo', methods=['GET','POST'])
def get_all_docs():
  if (request.method == 'POST') :
    some_json = request.get_json()
    doc = mongo.db.totalhelmetdata.find_one({'centreId' : some_json['centreId']},{'_id' : 0})
    totalRidesCompleted = doc['totalRidesCompleted'] + 1
    if (some_json['helmetReturned']) :
      totalHelmetsReturned = doc['totalHelmetsReturned'] + 1
    else : 
      totalHelmetsReturned = doc['totalHelmetsReturned']
    myQuery = {"centreId" : some_json['centreId']}
    doc = mongo.db.totalhelmetdata.update_one(myQuery, {"$set" : {"totalHelmetsReturned" : totalHelmetsReturned, "totalRidesCompleted" : totalRidesCompleted}})
    return jsonify({"message":"Data updated"})
  else :
    return jsonify({"message":"Please pass data"})