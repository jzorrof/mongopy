__author__ = 'joe_fan'
# -*- coding: utf-8 -*-
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
access collection Objects
"""
coll = db.dataset
coll = db['dataset']

