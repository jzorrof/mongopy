__author__ = 'joe_fan'
from pymongo import MongoClient

client =MongoClient()
db = client.chinese

cursor=db.zh.find()
for i in cursor:
    print i