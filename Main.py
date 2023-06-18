import os
from Vigenere import Vigenere
from OTP import OneTime

if(not os.path.exists("./OTP")):
    os.mkdir("./OTP")
if(not os.path.exists("./VGN")):
    os.mkdir("./VGN")

print("Cifrador / Decifrador - VER 1.0 - @ Mateus Leal")

vg = Vigenere()
otp = OneTime()
opc = ""

while(opc != "-1"):
    print("1- Cifrar um Arquivo")
    print("2- Decifrar um Arquivo")
    print()
    opc = input("Digite uma opção ou -1 para Sair: ")
    print()

    if(opc == "1"):
        print("1- Cifrar por Vigenére")
        print("2- Cifrar por One Time Pad")
        print()
        opc = input("Digite uma opção: ")
        print()
        
        if(opc == "1"):
            path = input("Digite o Caminho do Arquivo: ")
            key = input("Digite a chave de Encriptação: ")

            vg.criptografar(path,key)

        else:
            path = input("Digite o Caminho do Arquivo: ")

            otp.criptografar(path)


    elif(opc == "2"):
        print("1- Decifrar por Vigenére")
        print("2- Decifrar por One Time Pad")
        print()
        opc = input("Digite uma opção: ")
        print()

        if(opc == "1"):
            path = input("Digite o Caminho do Arquivo: ")
            key = input("Digite a chave de Encriptação: ")

            vg.decriptografar(path,key)

        else:
            path = input("Digite o Caminho do Arquivo: ")
            path_key = input("Digite o Caminho do Arquivo da Chave Encriptação: ")

            otp.decriptografar(path,path_key)