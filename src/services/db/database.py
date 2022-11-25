from pymongo import MongoClient

from settings import MONGO_DB_URL


client = MongoClient(MONGO_DB_URL)

db = client.movie_db
