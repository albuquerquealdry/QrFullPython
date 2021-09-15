import pymongo
from pymongo import MongoClient
import random
import string
import pyqrcode
import png
import sys
import os
from services import codeGerator

def login():
        key = input("Digite sua senha: ")
        client= MongoClient("mongodb://aldry:voppgdpt6zo8@db-32206.nuvem-us-04.absamcloud.com:17983/?authSource=testesaldry&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
        db = client.testesaldry
        user= db.user
        a= user.find_one({"password":key})
        dbResponse = a['password']
        if key == dbResponse:
            event=input("Para qual evento você deseja criar essa senha? ")
            convit=input("Qual o nome do seu convidado? ")
            codeGerator.qrCode(a['name'],a['password'],event, convit)
            os.system("python3 main.py")
        else:
            print("NOK")