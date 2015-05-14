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

# result = db.restaurants.update_one(
# {"name": "Juni"},
#     {
#         "$set":{
#             "cuisine": "American (New)"
#         },
#         "$currentDate": {"lastModified": True}
#     }
# )
#
# print result.matched_count

"""
Update an Embedded Field
"""

# result = db.restaurants.update_one(
#     {"restaurant_id": "41156888"},
#     {"$set": {"address.street": "East 31st Street"}}
# )
#
# print result.matched_count

"""
Update Multiple Documents
"""

# result = db.restaurants.update_many(
#     {
#         "address.zipcode": "10016", "cuisine": "Other"
#     },
#     {
#         "$set": {"cuisine": "Category To Be Determined"},
#         "$currentDate": {"lastModified": True}
#     }
# )
#
# print result.matched_count

"""
Replce Document
"""

result = db.restaurants.replace_one(
    {"restaurant_id": "41704620"},
    {
        "name": "Vella 2",
        "address": {
            "coord": [-73.9557413, 40.7720266],
            "building": "1480",
            "street": "2 Avenue",
            "zipcode": "10075"
        }
    }
)

print result.matched_count