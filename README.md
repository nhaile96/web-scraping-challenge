# web-scraping-challenge


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db= client.mars_db
collection=db.mars_sites

