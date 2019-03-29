from mlab import river_collection

rivers = list(river_collection.find({"continent":"Africa"}))
print(rivers)

