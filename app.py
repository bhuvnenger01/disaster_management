from flask import Flask
from routes import data_collection, data_processing, api
from config import Config
from flask_pymongo import PyMongo

# Initialize Flask app
app = Flask(__name__)

# Load config (DB, API keys, etc.)
app.config.from_object(Config)

# Initialize MongoDB connection
mongo = PyMongo(app)

# Register Blueprints (Routes)
app.register_blueprint(data_collection.bp)
app.register_blueprint(data_processing.bp)
app.register_blueprint(api.bp)

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
