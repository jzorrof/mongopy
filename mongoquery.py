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

for i in cursor:
    print i