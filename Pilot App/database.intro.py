from pymongo import MongoClient

# 1.Connect to mongodb

mongo_uri =  'mongodb+srv://admin:admin@c4e27-pilotapp-xjeyv.mongodb.net/test?retryWrites=true'

client = MongoClient(mongo_uri)

# 2. Get/Create Database

db_demo = client.test_database

# 3. Get/Create Collection

first_collection = db_demo['my_collection']

# 4. Create document

# game_document = {
#     'name':'Fo4',
#     'Description':'đá bóng'
# }

# # 5. Insert document

# first_collection.insert_one(game_document)

# 6. READ
# 6.1 READ all
# all_document = first_collection.find()
# print(all_document)

# for document in all_document :
#     print(document['name'])

# 6.2 READ one
one_document =  first_collection.find_one({'name':'LOL'})
print(one_document)