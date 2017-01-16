from pymongo import MongoClient


# connect to database
connection = MongoClient('localhost', 27017)

db = connection.video

# handle to names collection
names = db.movies

item = names.find_one()

print(item['title'])
