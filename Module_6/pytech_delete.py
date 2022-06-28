from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.7cjib.mongodb.net/test"
client=MongoClient(url)
mydb= client["pytech"]
data=mydb["Students"]
mydict=[{"student_id":1010,"first_name": "Tom","last_name": "Doe"}]
doc = data.find({})
print("displaying all documents from student collection")
for x in doc:
    print(x)
x=data.insert_many(mydict)
print("objests inserted with the fallowing ids",x.inserted_ids)
myquery={"student_id": 1010}
doc1=data.find_one(myquery)
print("displaying data for added Student with Student_id 1010:",doc1)
data.delete_one(myquery)
print("student 1010 has been deleted.")
doc = data.find({})
print("displaying all documents from student collection")
for x in doc:
    print(x)
print("program complete")