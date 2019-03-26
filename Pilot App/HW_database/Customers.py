from matplotlib import pyplot
from pymongo import MongoClient
mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)

db = client.get_database()

customers = db['customers']
event = 0
wom = 0 
ads = 0
# print(customers)
all_customers = list(customers.find())
# print(all_customers)
for customer in all_customers :
    if customer['ref'] == 'events' :
        event = event +1
    elif customer['ref'] == 'wom' :
        wom = wom + 1 
    else : 
        ads = ads + 1
print('event = ',event)
print('wom = ',wom)
print('ads = ',ads)

ref_type = [event,wom,ads]

ref_name = ['events','wom','ads']


pyplot.pie(ref_type , labels = ref_name, autopct='%.1f%%',explode=[0,0.01,0.02] )
pyplot.title('Customers are acquired from events, word of mouth, advertisments')
pyplot.axis('equal')
pyplot.show()
