__author__ = 'joe_fan'
# -*- coding: utf-8 -*-

from pymongo import MongoClient

"""
Aggregate
"""
client = MongoClient()
db = client.test

"""
Group Documents by a Field and Calculate Count
"""
cursor = db.restaurants.aggregate(
    [
        {"$group":{"_id":"$borough", "count":{"$sum":1}}}
    ]
)

for document in cursor:
    print(document)

"""
Filter and Group Documents
"""

cursor = db.restaurants.aggregate(
    [
        {"$match":{"borough":"Queens", "cuisine":"Brazilian"}},
        {"$group":{"_id":"address.zipcode","count":{"$sum":1}}}
    ]
)

for document in cursor:
    print(document)