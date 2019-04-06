from pymongo import MongoClient

mongo_uri= 'mongodb+srv://admin:<password>@c4e27-pilotapp-xjeyv.mongodb.net/test?retryWrites=true'


client = MongoClient(mongo_uri)

bike = client.bike

bike_collection = bike['bike']




