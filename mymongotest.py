# -*- coding: utf-8 -*-
__author__ = 'joe_fan'
from pymongo import MongoClient

client =MongoClient()
db = client.chinese

cursor=db.zh.insert({"name": "奇虎"})

cursor=db.zh.find()
for v, key in cursor:
    print v
    i=key.decode("unicode_escape");
    print i

