import string
import pyqrcode
import png
import os

def qrCode(name, password, event, convit ):
    directory= "\\gerateQRCodes"
    namedB = name
    passworddB= password
    eventdB= event
    convitdb= convit 
    qrcode = pyqrcode.create(namedB+"-"+eventdB+"-"+convitdb)
    qrcode.png(name+"-"+convit+"-"+event+".png", scale=6)