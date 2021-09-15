import os
from services import register, login, codeGerator

os.system("clear")
print("Olá seja bem vindo")
print("*"*20)
print("Essa tela é temporaria, em breve será uma aplicação web")
print("*"*56)
print ("selecione a opção:")
print("1- Registrar\n2-Entrar" )
selecao= input("selecioine a opção que deseja: ")
if selecao == "1":
    register.sendData()
if selecao =="2":
    login.login()
    