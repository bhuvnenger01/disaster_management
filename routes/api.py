from flask import Blueprint, jsonify
from flask_pymongo import PyMongo
from app import mongo

bp = Blueprint('api', __name__)

# API to get processed disaster data
@bp.route('/api/disasters', methods=['GET'])
def get_disaster_data():
    disasters = mongo.db.disasters.find()
    result = [{"type": disaster['type'], "location": disaster['location']} for disaster in disasters]
    return jsonify(result)
