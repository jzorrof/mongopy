__author__ = 'joe_fan'
# -*- coding: utf-8 -*-

from pymongo import MongoClient

"""
Aggregate
"""
client = MongoClient()
db = client.test

cursor = db.restaurants.aggregate(
    [
        {"$group":{"_id":"$borough", "count":{"$sum":1}}}
    ]
)

for document in cursor:
    print(document)