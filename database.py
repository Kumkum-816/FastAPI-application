from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://kumkumpatel64:0SMHm4HtXy88ZPB9@cluster0.xysjt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.key_value_store
collection = db.store
