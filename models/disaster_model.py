from app import mongo

# Insert disaster data
def insert_disaster(data):
    mongo.db.disasters.insert_one(data)

# Find all disaster data
def get_all_disasters():
    return mongo.db.disasters.find()
