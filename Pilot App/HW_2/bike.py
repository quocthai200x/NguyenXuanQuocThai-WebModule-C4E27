from pymongo import MongoClient

mongo_uri =  'mongodb+srv://admin:admin@c4e27-pilotapp-xjeyv.mongodb.net/test?retryWrites=true'

client = MongoClient(mongo_uri)

pilot_app = client.bikes

bike_collection = pilot_app['my_bike']

