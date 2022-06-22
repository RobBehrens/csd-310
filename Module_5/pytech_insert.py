from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.7cjib.mongodb.net/test"
client=MongoClient(url)
mydb= client["pytech"]
data=mydb["Students"]
mydict=[{"student_id":1007,"first_name": "John","last_name": "Dalton"},{"student_id":1008,"first_name": "Jack","last_name": "Anderson"},{"student_id":1009,"first_name": "Micheal","last_name": "Mckay"}]
x=data.insert_many(mydict)
print("objests inserted with the fallowing ids",x.inserted_ids)
print("program complete")