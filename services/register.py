import os
import random
import random
import string
import pymongo
from pymongo import MongoClient
import datetime
import pprint
from services import sendEmail
import time

def sendData():
    name = input("Digite seu nome: ")
    email = input("email: ")
    os.system("clear")
    if name and email != "":
        size = 16
        chars = string.ascii_letters + string.digits + '!@#$%&*()+-?'
        rnd = random.SystemRandom()
        password = (''.join(rnd.choice(chars) for i in range(size)))
        dateRegister = datetime.datetime.now()

        client= MongoClient("mongodb://aldry:voppgdpt6zo8@db-32206.nuvem-us-04.absamcloud.com:17983/?authSource=testesaldry&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
        db = client.testesaldry
        db.user.insert_one({
                "name": name,
                "email": email,
                "password": password,
                "date": dateRegister
                })
        db = client.testesaldry
        db.emailList.insert_one({
                "email": email
                })
        
        print ("Sua chave foi enviada por email")
        sendEmail.sendemail(password,name, email)
        time.sleep(3)
        os.system("python3 main.py")
