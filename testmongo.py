__author__ = 'joe_fan'
# -*-uft
from pymongo import MongoClient

"""
connection demo
"""
client = MongoClient()
client = MongoClient("mongodb://mongodb0.example.net:27019")

"""
access db objects
"""
db = client.primer
db = client['primer']

"""
accesse collection Objects
"""
coll = db.dataset
coll = db['dataset']