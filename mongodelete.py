__author__ = 'joe_fan'
# -*- coding: utf-8 -*-

from pymongo import MongoClient

"""
Create connection
"""
client = MongoClient()
db = client.test

"""
Remove all documents that match a condition
"""
result = db.restaurants.delete_many({"borough": "Manhattan"})

result.deleted_count

"""
Remove all Documents
"""
result = db.restaurants.delete_many({})

result.deleted_count

"""
Drop a collection
"""
db.restaurants.drop()

