from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.7cjib.mongodb.net/test"
client=MongoClient(url)
db=client.pytech
collections=db.list_collection_names()
print("-- Pytech Collection list --")
print(collections)