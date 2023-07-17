import pymongo
#connect to mongoDb
client=pymongo.MongoClient()
#create a database
 
tdb= client["test_database"]

#create a collection in the database

tcoll= tdb["person"]
#create a document 

tdoc= {"name": "hajra shahid", "age": 21}

#add a document
x=tcoll.insert_one(tdoc)
tdoc1=[{"name": "Mahnoor Asif", "age": 22},{"name": "kanwal asif", "age": 23}]

x=tcoll.insert_many(tdoc1)

document = tcoll.find_one({"name": "hajra shahid"})
print("Single document:", document)