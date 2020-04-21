from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['teststore']
collection = db['products']

collection.insert_one({"_id": 2,"name": "teclado", "price": 300})
collection.insert_one({"_id": 3, "nombre": "monitor", "precio": 200})