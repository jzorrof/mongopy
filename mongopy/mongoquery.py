__author__ = 'joe_fan'
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pymongo

'''
create connection
'''
client = MongoClient()
db = client.test

"""
create cursor
"""
# cursor = db.restaurants.find()

"""
query all ... too much data
"""
# for i in cursor:
# print i

"""
query by top level field
"""

# cursor = db.restaurants.find({"borough":"Manhattan"})
# for i in cursor:
#     print(i)

"""
query by a field in
1.an Embedded Document
2.Aarry
"""
# cursor = db.restaurants.find({"address.zipcode":"10075"})
# for i in cursor:
#     print i
# cursor = db.restaurants.find({"grades.grade": "B"})
# for i in cursor:
#     print i

"""
user operator
{ <field1>: { <operator1>: <value1> } }
"""
# cursor = db.restaurants.find({"grades.score":{"$lt": 10}})
# for i in cursor:
#     print i
"""
Logical AND and OR
"""
# cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})
# for i in cursor:
#     print i

# cursor = db.restaurants.find({"$or": [{"cuisine": "Italian", "address.zipcode": "10075"}]})
# for i in cursor:
#     print i

"""
sort()
"""
cursor = db.restaurants.find().sort(
    [
        ("borough", pymongo.ASCENDING),
        ("address.zipcode", pymongo.DESCENDING)
    ]
)

for i in cursor:
    print i