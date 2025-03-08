from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb+srv://detectionplate:Detection11@detplat.0zrfc.mongodb.net/?retryWrites=true&w=majority&appName=detPlat")
db = client["traffic_violation_db"]
collection = db["vehicle_owners"]
