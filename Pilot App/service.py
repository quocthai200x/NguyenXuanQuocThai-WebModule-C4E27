from pymongo import MongoClient
from faker import Faker
from random import randint,choice
faker = Faker()

mongo_uri =  'mongodb+srv://admin:admin@c4e27-pilotapp-xjeyv.mongodb.net/test?retryWrites=true'

client = MongoClient(mongo_uri)

pilot_app = client.db_pilot

services = pilot_app['services']
for i in range(50):
    new_service = {
        'name': faker.name(),
        'Tuổi':randint(18,30),
        'Giới tính':choice(['Male','Female']),
        'Chiều cao':randint(160,180),
        'available':choice(['Yes','No']),
        'address':faker.address()
    }

    services.insert_one(new_service)
    print('Saving document {0}.......'.format(i+1))