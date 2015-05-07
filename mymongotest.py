# -*- coding: utf-8 -*-
__author__ = 'joe_fan'
from pymongo import MongoClient

client =MongoClient()
db = client.chinese

cursor=db.zh.insert({"name": "奇虎"})

cursor=db.zh.find()
for i in cursor:
    print i

