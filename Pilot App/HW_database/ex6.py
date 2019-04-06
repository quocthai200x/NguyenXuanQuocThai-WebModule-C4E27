from mlab import river_collection


rivers = river_collection.find()
for river in rivers :
    if river['continent'] == 'S. America' :
        if river['length'] < 1000 :
            print('abc')
print(rivers)
