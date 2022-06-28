from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.7cjib.mongodb.net/test"
client=MongoClient(url)
mydb=client["pytech"]
data=mydb["Students"]
myquery={"student_id": 1007}
alterdata={"$set": {"last_name": "doe"}}
doc = data.find({})
print("displaying all documents from student collection")
for x in doc:
    print(x)
data.update_one(myquery, alterdata)

doc=data.find_one(myquery)
print("displaying  upated data for Student with Student_id 1007:",doc)