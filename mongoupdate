__author__ = 'joe_fan'
# -*- coding: utf-8 -*-
from pymongo import MongoClient

"""
connect
"""
client = MongoClient()
db = client.test

"""
Update Top-Level Fields
"""

result = db.restaurants.update_one(
    {"name": "Juni"},
    {
        "$set":{
            "cuisine": "American (New)"
        },
        "$currentDate": {"lastModified": True}
    }
)

result.matched_count