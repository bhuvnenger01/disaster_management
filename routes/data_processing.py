from flask import Blueprint, jsonify
from services.ml_service import classify_data

bp = Blueprint('data_processing', __name__)

# Route for processing and classifying data
@bp.route('/process', methods=['POST'])
def process_data():
    classified_data = classify_data()
    return jsonify(classified_data)
