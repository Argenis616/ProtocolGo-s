import socket, threading
from model.poke_base import *
from struct import pack, unpack
from model.codes import *
from model.poke_api import *
import random
from PIL import Image
import os
import base64

def ini(csocket):
    """
    socket is created to establish communication
    Args:
        csocket: We pass the socket as a parameter.
    """
    trainers = get_trainers()
    csocket.sendall(bytes(trainers,"utf-8"))

def menu(csocket,trainer):
    """
    We define the menu
    Args:
        csocket: We pass the socket  as a parameter.
        trainer: We pass the trainer as a parameter.
    """
    welcome = get_name_trainer(trainer)
    ini = "Bienvenido: "+ welcome +"\n Selecciona una opcion: \n"+ "1 Captura Pokemon \n" + "2 Ver Pokedex \n" + "3 Cerrar Sesion \n"
    csocket.sendall(bytes(ini,"utf-8"))

def show_pokemon(csocket,trainer):
    """
    This funcion shows a pokemon randomly and We define the range from one to four hundred.
    Args:
        csocket: We pass the socket  as a parameter.
        trainer: We pass the trainer as a parameter.
    """
    number_poke = random.randrange(1,400)
    poke = show_name(number_poke)
    election = "Oh! un " + poke + " Salvaje a aparecido"
    csocket.send(bytes(election, "utf-8"))
    elec = "Deseas capturar al pokemon: " + "," + poke + "," + (str(number_poke)) + "," + "?"    
    separator = ","
    string_separated = elec.split(separator)
    print(string_separated)
    csocket.send(bytes(string_separated[2], "utf-8"))

def show_pokedex(csocket,trainer):
    """
    We show a list with the pokemon was captured.
    Args:
        csocket: We pass the socket  as a parameter.
        trainer: We pass the trainer as a parameter.
    """
    pokedex ="Tus Pokemon son: \n" +  get_pokedex(trainer)
    csocket.sendall(bytes(pokedex,"utf-8"))

def capture_pokemon(csocket,trainer,pokemon):
    """
    You can capture pokemon with this function
    Args:
        csocket: We pass the socket  as a parameter.
        trainer: We pass the trainer as a parameter.
        pokemon: We pass the pokemon as a parameter.
    """
    range_capture = random.randrange(1,3)
    if 1 == 1:
        trainer =int(trainer)
        set_pokedex(pokemon,str(trainer))
        print(trainer,pokemon)
        obtain_img_pokemon(pokemon)
        image = open(pokemon + ".png", 'rb')
        image_read = image.read()
        image_64_encode = base64.encodestring(image_read)
        csocket.sendall(image_64_encode)
        name_pokemon = show_name(pokemon)
        csocket.sendall(bytes(str(name_pokemon), "utf-8"))

    else:
        csocket.sendall(bytes(str(NO_CAPTURE),"utf-8"))



class ClientThread(threading.Thread):
    """
    This class is defined due to We can have many clients.
    """
    def __init__(self,clientAddress,clientsocket):
        """
        We define the class'constructor method
        Args:
            self: With self you can make references to class attributes.
            clientAddress: We pass the client address as a parameter.
            clientsocket: We pass the client socket as a parameter.
        """
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        """
        We split the codes
        self: With self you can make references to class attributes.
        """
        while True:
            codes = self.csocket.recv(1024)
            code = codes.decode("utf-8")[0:2]
            code_id = codes.decode("utf-8")[2:4]
            img = codes.decode("utf-8")[4:]
            if code == "0":
              break
            if code == "11":
                menu(self.csocket,code_id)
            elif code == "12":
                ini(self.csocket)
            elif code == "20":
                show_pokemon(self.csocket,code_id)
            elif code == "24":
                show_pokedex(self.csocket,code_id)
            elif code == "30":
                capture_pokemon(self.csocket,code_id,img)
            else:
                print("Error en la conexion")
                self.csocket.close()
            print ("from client", code, clientAddress)
        print ("Client at ", clientAddress , " disconnected...")

LOCALHOST = input("ingresa el server donde se encuentar puede ser localhost  o 192.168.1.1\n")
PORT = input("ingresa el puerto puede ser 9999\n")
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, int(PORT)))
    print("Server started")
    print("Waiting for client request..")
finally:
    print("Lo sentimos no podemos levantar el servicio")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
