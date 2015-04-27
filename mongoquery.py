__author__ = 'joe_fan'
# -*- coding: utf-8 -*-

from pymongo import MongoClient
'''
create connetction
'''
client = MongoClient()
db = client.test

"""
create cursor
"""
cursor = db.restaurants.find()


"""
query all ... too much data
"""
# for i in cursor:
#     print i

"""
query by top level field
"""

cursor = db.restaurants.find({"borough":"Manhattan"})
for i in cursor:
    print(i)