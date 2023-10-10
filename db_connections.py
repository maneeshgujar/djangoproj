import pymongo

url='mongodb+srv://maneesh_01:dTAoru674pRYEG6H@cluster0.ipwkq5z.mongodb.net/djangoproj'

client= pymongo.MongoClient(url)

# db = client['djangoproj']

db = client.get_database()