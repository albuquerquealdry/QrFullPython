import os
import sys
import hashlib

def createDiretory():
    file = sys.argv[1]
    resultado = hashlib.md5(file.encode('utf-8'))
    filemd5=(resultado.hexdigest())
    os.mkdir(filemd5)