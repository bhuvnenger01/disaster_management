from flask import Blueprint, jsonify
from services.twitter_service import get_twitter_data
from services.news_service import get_news_data

bp = Blueprint('data_collection', __name__)

# Route to collect data from Twitter
@bp.route('/collect/twitter', methods=['GET'])
def collect_twitter_data():
    data = get_twitter_data()
    return jsonify(data)

# Route to collect data from news portals
@bp.route('/collect/news', methods=['GET'])
def collect_news_data():
    data = get_news_data()
    return jsonify(data)
