from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)
db = client.c4e
post = db['posts']

post_document = {
    'title':'Admin bộ giáo dục',
    'author':'>.< ai cho mà biết',
    'content':'Mai nghỉ học nhé Quân :)) .giờ quất thôi'
}

post.insert_one(post_document)