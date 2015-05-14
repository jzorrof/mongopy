# -*- coding: utf-8 -*-
__author__ = 'joe_fan'
from pymongo import MongoClient

client =MongoClient()
db = client.chinese

cursor=db.zh.insert({"name": "Jone"})

cursor=db.zh.find()
for i in cursor:
    for key, value in i.items():
        print key
        # i=key.decode("unicode_escape");
        print value

