import socket
from struct import pack, unpack
from model.codes import *
import os
from PIL import Image
import base64
import random
from io import BytesIO

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.timeout(10)
def init_Pokemon():
    """
    We show the initial logo
    """
    start = "\n" +"""
        _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
        \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
         \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
           \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
            \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
             \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
              \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
               \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
                \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                        `'                            '-._|
        """
    return start
def final_logo():
    """
    We show the final logo
    """
    final = "\n" + """
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::-'    `-::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::-'          `::::::::::::::::
:::::::::::::::::::::::::::::::::::::::-  '   /(_M_)\  `:::::::::::::::
:::::::::::::::::::::::::::::::::::-'        |       |  :::::::::::::::
::::::::::::::::::::::::::::::::-         .   \/~V~\/  ,:::::::::::::::
::::::::::::::::::::::::::::-'             .          ,::::::::::::::::
:::::::::::::::::::::::::-'                 `-.    .-::::::::::::::::::
:::::::::::::::::::::-'                  _,,-::::::::::::::::::::::::::
::::::::::::::::::-'                _,--:::::::::::::::::::::::::::::::
::::::::::::::-'               _.--::::::::::::::::::::::#####:::::::::
:::::::::::-'             _.--:::::::::::::::::::::::::::#####:::::####
::::::::'    ##     ###.-::::::###:::::::::::::::::::::::#####:::::####
::::-'       ###_.::######:::::###::::::::::::::#####:##########:::####
:'         .:###::########:::::###::::::::::::::#####:##########:::####
     ...--:::###::########:::::###:::::######:::#####:##########:::####
 _.--:::##:::###:#########:::::###:::::######:::#####:#################
'#########:::###:#########::#########::######:::#####:#################
:#########:::#############::#########::######:::#######################
##########:::########################::################################
##########:::##########################################################
##########:::##########################################################
#######################################################################
#######################################################################
################################################################# dp ##
#######################################################################
"""
    return final
def ini():
    """
    Protocol is started.
    """
    codes = bytes(str(INIT_PROTOCOL),"utf-8")
    code_id = bytes(str(INIT_PROTOCOL),"utf-8")
    img = bytes(str(INIT_PROTOCOL),"utf-8")
    client.sendall(codes + code_id + img)
    print(init_Pokemon())
    elecd = client.recv(1024)
    print(elecd.decode("utf-8"))
    while True:
        try:
            elec = input("Elige: ")
            elec1 = int(elec)
            break
        except ValueError:
            print("No es una opcion")
            ini()
            pass
        return elec
    if elec1 == 0 or elec1 not in range(1,4):
        print(final_logo())
        print("Regresa cuando quieras tus pokemon te esperan.")
        client.close()
    else:
        trainer(elec)

def trainer(elec):
    """
    Trainer's options are defined.
    Args:
        elec: We pass the trainer as a parameter.
    """
    codes = bytes(str(TRAINER_CHOOSE),"utf-8")
    code_id = bytes("0"+elec,"utf-8")
    img = bytes(str(TRAINER_CHOOSE),"utf-8")
    client.sendall(codes + code_id + img)
    al = client.recv(1024)
    print(al.decode("utf-8"))
    pokemon(elec)

def pokemon(elec):
    """
    Pokemon's options are defined.
    Args:
        elec: We pass the trainer as a parameter.
    """
    elec1 = input("Elige una opcion: ")
    if elec1 == "1":
        election(elec)
    elif elec1 == "2":
        codes = bytes(str(SHOW_POKEDEX),"utf-8")
        code_id = bytes("0"+elec,"utf-8")
        img = bytes(str(SHOW_POKEDEX),"utf-8")
        client.sendall(codes + code_id + img)
        al = client.recv(1024)
        print(al.decode("utf-8"))
        print()
        ele1 = input("Si decseas salir escribe salir: ")
        if ele1 == "salir":
            trainer(elec)
        else:
            print("Lo siento invalido pero me caes bien adios :) ")
            trainer(elec)
    elif elec1 == "3":
        print("Hasta luego entrenador vuelve pronto")
        ini()
    else:
        print("Opcion invalida: ")
        trainer(elec)

def election(elec):
    """
    We define the main menu that We show the user.
    Args:
        elec: We pass the trainer as a parameter.
    """
    codes = bytes(str(CHOOSE_POKEMON),"utf-8")
    code_id = bytes("0"+elec,"utf-8")
    img = bytes(str(CHOOSE_POKEMON),"utf-8")
    client.sendall(codes + code_id + img)
    al = client.recv(1024)
    print(al.decode("utf-8"))
    alg = client.recv(1024)
    number_poke = alg.decode("utf-8")
    number_of_attemps = random.randrange(1,10)
    print("Tienes " + str(number_of_attemps) + " Pokebolas para traparlo")
    elc1 = input("Deseas capturarlo SI o NO o ESCAPAR: ")
    if elc1 == "SI":
        range_capture(elec, number_poke, number_of_attemps)
    elif elc1 == "NO":
        election(elec)
    elif elc1 == "ESCAPAR":
        print("Hasta luego!")
        trainer(elec)
    else:
        print("Opcion invalida vuelve pronto ")
        trainer(elec)

def range_capture(elec,number_poke,number_of_attemps):
    """
    We define the capture range
    Args:
        elec: We pass the trainer as a parameter.
        number_poke: We pass the pokemon's identification as a parameter.
        number_of_attemps: We pass the number of attemps as a parameter.
    """
    if number_of_attemps != 0:
        codes = bytes(str(CHOOSE_YES),"utf-8")
        code_id = bytes("0"+elec,"utf-8")
        img = bytes(str(number_poke),"utf-8")
        client.sendall(codes + code_id + img)
        al = client.recv(2048)
        alg = al.decode("utf-8")
        if alg == str(NO_CAPTURE):
            number_of_attemps = number_of_attemps  - 1
            print ("Ups se salio de la pokebola!\n Deseas intentarlo de nuevo?\n Te quedan "+ str(number_of_attemps) +" Pokebolas")
            var  = input("SI o NO: ")
            if var == "SI":
                range_capture(elec,number_poke,number_of_attemps)

            else:
                election(elec)
        else:
            name_pokemon = client.recv(1024)
            name_pokemon = name_pokemon.decode("utf-8")

            print("Pokemon capturado")
            
            dir = os.getcwd() 
            
            if not os.path.exists(dir + "/Pokedex"):
                pwd = os.mkdir(dir + "/Pokedex")
                image_decode = Image.open(BytesIO(base64.decodestring(al)))
                image_decode.save(dir +"/Pokedex/" + str(name_pokemon) + ".png", 'PNG')
                img = Image.open(dir +"/Pokedex/" + str(name_pokemon) + ".png")
                img.show(dir +"/Pokedex/" + str(name_pokemon) + ".png")
                print("La imagen ya esta en tu Pokedex\n Tu ruta es: ")
                print(dir + "/Pokedex/" + str(name_pokemon) + ".png")
                trainer(elec)
            else: 
                print("La imagen ya esta en tu Pokedex\n Tu ruta es: ")
                image_decode = Image.open(BytesIO(base64.decodestring(al)))
                image_decode.save(dir +"/Pokedex/" + str(name_pokemon) + ".png", 'PNG')
                img = Image.open(dir +"/Pokedex/" + str(name_pokemon) + ".png")
                img.show(dir + "/Pokedex/" + str(name_pokemon) + ".png")
                print(dir + "/Pokedex/" + str(name_pokemon) + ".png")
                trainer(elec)
    else:
        print("Ups que tramposo ya no tenias pokebolas.")
        trainer(elec)


def main():
    """
    Function that establishes the connection of the client with the server
    through a socket.
    """
    try:
        print ("Ingresa el servidor al que deseas ingresar:\n")
        print ("Un ejemplo seria localhost o 192.168.1.1 \n")
        SERVER = input()
        print ("Ingresa el puerto que te debes conectar un ejemplo seria 9999\n")
        PORT = input()

        client.connect((SERVER,int(PORT)))
        ini()
    finally:
        print("Lo sentimos problemas con la conexion intentalo de nuevo")
        client.close()

if __name__ == "__main__":
    main()