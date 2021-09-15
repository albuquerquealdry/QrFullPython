import hashlib
import sys
import pymongo
from pymongo import MongoClient
import datetime

user = sys.argv[2]
file= sys.argv[3]
resultado = hashlib.md5(file.encode('utf-8'))
filemd5=(resultado.hexdigest())

client= MongoClient("mongodb://aldry:voppgdpt6zo8@db-32206.nuvem-us-04.absamcloud.com:17983/?authSource=testesaldry&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db = client.testesaldry
date = datetime.datetime.now()
db.filesRegister.insert_one({
        "user": user,
        "date":date,
        "fileNameNative": file,
        "fileNameMD5": filemd5
        })
